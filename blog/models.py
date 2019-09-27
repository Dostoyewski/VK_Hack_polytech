from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify

start_num = -1

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class UserProfile(models.Model):
    #Неизменяемые
    events_registered = models.CharField(max_length=1000, blank=True)
    karma = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Изменяемые
    user_url = models.SlugField(max_length=200, unique=True)
    bio = models.TextField(max_length=500, blank=True, default='Не заполнено')
    location = models.CharField(max_length=30, default='Не указан')
    birth_date = models.DateField(null=True, blank=True)
    vorname = models.CharField(max_length=20, blank=True)
    nachname = models.CharField(max_length=50, blank=True)
    urlVK = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(null=False, blank=True)
    extended_profile = models.BooleanField(default=False)

    def __str__(self):  
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
        profile, created = UserProfile.objects.get_or_create(user=instance)
        profile.user_url = slugify(profile.user.email+profile.user.first_name)
        profile.save()

post_save.connect(create_user_profile, sender=User) 


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    beginning_at = models.DateTimeField()
    ending_at = models.DateTimeField()
    users_registered = models.CharField(max_length=10000, blank=True)
    min_karma = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

