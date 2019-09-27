from django.views import generic
from .models import Post, UserProfile
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ChangeForm
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
    event = Post.objects.get(slug=slug)
    is_reg = False
    karma_check = True
    try:
        profile = UserProfile.objects.get(user_id=request.user.pk)
        evreg = profile.events_registered.split(sep=', ')
        if str(event.pk) in evreg:
            is_reg = True
        if profile.karma < event.min_karma:
            karma_check = False
    except:
        pass
    return render(request, 'post_detail2.html', {'title': event.title, 'beginning_at': event.beginning_at, 'ending_at': event.ending_at,
                                                'author': event.author, 'created_on': event.created_on, 'content': event.content, 
                                                'is_reg': is_reg, 'ka_ch': karma_check})

def acc_det(request):
    #Дефолтные поля не предусмотрены. Ввод ссылок только с http
    try:
        a = UserProfile.objects.get(user_id=request.user.pk)
        pk = a.pk
        bio = a.bio
        location = a.location
        birth_date = a.birth_date
        karma = a.karma
        vorname = a.vorname
        nachname = a.nachname
        urlVK = a.urlVK
        phone = a.phone
        mail = request.user.email
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
                                            'urlVK': urlVK, 'phone': phone, 'mail': mail})

def change(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST)
        if form.is_valid():
            profile = UserProfile.objects.get(user_id=request.user.pk)
            profile.bio = form.cleaned_data['bio']
            profile.birth_date = form.cleaned_data['birth_date']
            profile.vorname = form.cleaned_data['vorname']
            profile.nachname = form.cleaned_data['nachname']
            profile.urlVK = form.cleaned_data['urlVK']
            profile.phone = form.cleaned_data['phone']
            profile.save()
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = ChangeForm()
    return render(request, 'change.html', {'form': form})

def event_register(request, slug):
    '''Функция регистрации на событие'''
    event = Post.objects.get(slug=slug)
    profile = UserProfile.objects.get(user_id=request.user.pk)
    if profile.karma >= event.min_karma:
        event.users_registered += str(request.user.pk)+', '
        profile.events_registered += str(event.pk) + ', '
        profile.save()
        event.save()
    return HttpResponseRedirect('/'+slug)

#Дописать функцию сортировки!!
@login_required
def my_events(request):
    profile = UserProfile.objects.get(user_id=request.user.pk)
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

@login_required
def my_arhive(request):
    profile = UserProfile.objects.get(user_id=request.user.pk)
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
