from django.views import generic
from .models import Post, UserProfile
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ChangeForm, CommentForm, ApproveForm, RegCommentForm
from django.contrib.auth.decorators import login_required
import datetime
import pytz
from .mes_confirmation import sent_verification_code

utc=pytz.UTC

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

#Страница рендерилась на основе модели объекта
#Изменена на функциональное задание
#class PostDetail(generic.DetailView):
#    model = Post
#    template_name = 'post_detail.html'

def PostDetail(request, slug):
    if slug == 'users':
        last_pk = UserProfile.objects.last().pk+1
        uprofiles = []
        for i in range(0, last_pk):
            try:
                uprofiles.append(UserProfile.objects.get(pk=i))
            except:
                pass
        return render(request, 'users.html', {'uprofiles': uprofiles})
    else:
        event = Post.objects.get(slug=slug)
        is_reg = False
        karma_check = True
        is_full = False
        can_vote = False
        users_ids = event.users_registered.split(sep=', ')
        uprofiles = []
        for idd in users_ids:
            try:
                uprofiles.append(UserProfile.objects.get(user_id=int(idd)))
            except:
                pass
        try:
            profile = UserProfile.objects.get(user_id=request.user.pk)
            is_full = profile.extended_profile
            if profile.karma_counts > 0:
                can_vote = True
            evreg = profile.events_registered.split(sep=', ')
            if str(event.pk) in evreg:
                is_reg = True
            if profile.karma < event.min_karma:
                karma_check = False
        except:
            pass
        return render(request, 'post_detail2.html', {'title': event.title, 'beginning_at': event.beginning_at, 'ending_at': event.ending_at,
                                                    'author': event.author, 'created_on': event.created_on, 'content': event.content, 
                                                    'is_reg': is_reg, 'ka_ch': karma_check, 'uprofiles': uprofiles, 'can_vote': can_vote})

def acc_det(request, slug):
    #Дефолтные поля не предусмотрены. Ввод ссылок только с http
    try:
        slpk = UserProfile.objects.get(user_url=slug).pk 
        repk = UserProfile.objects.get(user_id=request.user.pk).pk
        is_this_user = slpk == repk
    except:
        is_this_user = False
    try:
        a = UserProfile.objects.get(user_url=slug)
        pk = a.pk
        bio = a.bio
        location = a.location
        birth_date = a.birth_date
        karma = a.karma
        vorname = a.vorname
        nachname = a.nachname
        urlVK = a.urlVK
        phone = a.phone
        mail = a.user.email
    except:
        pk = None
        bio = None
        location = None
        birth_date = None
        karma = None
        vorname = None
        nachname = None
        urlVK = None
        phone = None
        mail = None

    return render(request, 'account.html', {'data': pk, 'bio': bio, 'location': location,
                                            'birth_date': birth_date, 'karma': karma,
                                            'vorname': vorname, 'nachname': nachname,
                                            'urlVK': urlVK, 'phone': phone, 'mail': mail, 
                                            'flag': is_this_user, 'slug': slug})

def change(request, slug):
    try:
        slpk = UserProfile.objects.get(user_url=slug).pk 
        repk = UserProfile.objects.get(user_id=request.user.pk).pk
        is_this_user = slpk == repk
    except:
        is_this_user = False
    if request.method == 'POST':
        profile = UserProfile.objects.get(user_id=request.user.pk)
        form = ChangeForm(request.POST, initial={'bio': profile.bio, 'vorname': profile.vorname, 'nachname': profile.nachname,
                                                 'location': profile.location, 'birth_date': profile.birth_date, 'urlVK': profile.urlVK,
                                                 'phone': profile.phone})
        if form.is_valid():
            profile = UserProfile.objects.get(user_id=request.user.pk)
            profile.bio = form.cleaned_data['bio']
            profile.birth_date = form.cleaned_data['birth_date']
            profile.vorname = form.cleaned_data['vorname']
            profile.nachname = form.cleaned_data['nachname']
            if form.cleaned_data['urlVK'][:7] == 'http://':
                profile.urlVK = form.cleaned_data['urlVK']
            else:
                profile.urlVK = 'http://' + form.cleaned_data['urlVK']
            profile.phone = form.cleaned_data['phone']
            profile.extended_profile = True
            profile.location = form.cleaned_data['location']
            # ЭТА ХУИТА НЕ РАБОТАЕТ
            #profile.profile_image = form.cleaned_data['profile_image']
            profile.save()
            return HttpResponseRedirect('/users/'+slug)
    else:
        profile = UserProfile.objects.get(user_id=request.user.pk)
        form = ChangeForm(initial={'bio': profile.bio, 'vorname': profile.vorname, 'nachname': profile.nachname,
                                                 'location': profile.location, 'birth_date': profile.birth_date, 'urlVK': profile.urlVK,
                                                 'phone': profile.phone})
    return render(request, 'change.html', {'form': form, 'flag': is_this_user, 'slug': slug})

def event_register(request, slug):
    '''Функция регистрации на событие'''
    event = Post.objects.get(slug=slug)
    profile = UserProfile.objects.get(user_id=request.user.pk)
    now = utc.localize(datetime.datetime.now())
    if profile.karma >= event.min_karma and now <= event.beginning_at:
        event.users_registered += str(request.user.pk)+', '
        profile.events_registered += str(event.pk) + ', '
        profile.save()
        event.save()
    return HttpResponseRedirect('/'+slug)


#Редиректы
def redirect_to_profile(request):
    try:
        slug = UserProfile.objects.get(user_id=request.user.pk).user_url
        return HttpResponseRedirect('/users/'+slug)
    except:
        return HttpResponseRedirect('/')

def redirect_to_event(request):
    try:
        slug = UserProfile.objects.get(user_id=request.user.pk).user_url
        return HttpResponseRedirect('/users/'+slug+'/events')
    except:
        return HttpResponseRedirect('/')

def redirect_to_change(request):
    try:
        slug = UserProfile.objects.get(user_id=request.user.pk).user_url
        return HttpResponseRedirect('/users/'+slug+'/change')
    except:
        return HttpResponseRedirect('/')

def redirect_to_arhive(request):
    try:
        slug = UserProfile.objects.get(user_id=request.user.pk).user_url
        return HttpResponseRedirect('/users/'+slug+'/arhive')
    except:
        return HttpResponseRedirect('/')

def my_events(request, slug):
    profile = UserProfile.objects.get(user_url=slug)
    evreg = profile.events_registered.split(sep=', ')
    names = []
    now = utc.localize(datetime.datetime.now())
    for key in evreg:
        try:
            key = int(key)
            if Post.objects.get(pk=key).ending_at > now:
                names.append('"'+Post.objects.get(pk=key).title+'"' + ', ' + 'дата начала: ' + str(Post.objects.get(pk=key).beginning_at))
        except ValueError:
            pass
    return render(request, 'events.html', {'data': names, 'length': len(names)})

def my_arhive(request, slug):
    profile = UserProfile.objects.get(user_url=slug)
    evreg = profile.events_registered.split(sep=', ')
    names = []
    now = utc.localize(datetime.datetime.now())
    for key in evreg:
        try:
            key = int(key)
            if Post.objects.get(pk=key).ending_at < now:
                names.append('"'+Post.objects.get(pk=key).title+'"' + ', ' + 'дата начала: ' + str(Post.objects.get(pk=key).beginning_at))
        except ValueError:
            pass
    return render(request, 'arhive.html', {'data': names, 'length': len(names)})

@login_required
def karmaplus(request, slug):
    now = utc.localize(datetime.datetime.now())
    user_profile = UserProfile.objects.get(user_id=request.user.pk)
    comment_profile = UserProfile.objects.get(user_url=slug)
    if now.hour == 0 and now.minute == 0:
        user_profile.karma_counts = 5
        user_profile.save()
    if user_profile.karma >= 0 and user_profile != comment_profile and user_profile.karma_counts > 0:
        comment_profile.karma += 0.1
        user_profile.karma_counts -= 1
        user_profile.save()
        comment_profile.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def karmaminus(request, slug):
    now = utc.localize(datetime.datetime.now())
    user_profile = UserProfile.objects.get(user_id=request.user.pk)
    comment_profile = UserProfile.objects.get(user_url=slug)
    if now.hour == 0 and now.minute == 0:
        user_profile.karma_counts = 5
        user_profile.save()
    if user_profile.karma >= 0 and user_profile != comment_profile and user_profile.karma_counts > 0:
        comment_profile.karma -= 0.1
        user_profile.karma_counts -= 1
        user_profile.save()
        comment_profile.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
'''
def approve_comment(request):
    if request.method == 'POST':
        form = ApproveForm(request.POST)
        if form.is_valid():
            scode = form.cleaned_data['code']
            if scode == code:
                return HttpResponseRedirect('/')
            else:
                form = ApproveForm()
    else:
        form = ApproveForm()
    return render(request, 'comment_approve.html', {'form': form, 'code': code})'''