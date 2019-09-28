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
    karma = models.FloatField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    karma_counts = models.IntegerField(default=5)
    user_url = models.SlugField(max_length=200, unique=True)
    #Изменяемые
    bio = models.TextField(max_length=500, blank=True, default='Не заполнено')
    location = models.CharField(max_length=30, default='Не указан')
    birth_date = models.DateField(null=True, blank=True)
    vorname = models.CharField(max_length=20, blank=True)
    nachname = models.CharField(max_length=50, blank=True)
    urlVK = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(null=False, blank=True)
    #Место учебы/работы
    work_place = models.TextField(max_length=500, blank=True, default='Не заполнено')
    #Специальность по диплому
    specialization = models.TextField(max_length=500, blank=True, default='Не заполнено')
	#Какими иностранными языками Вы владеете (укажите уровень владения)? 
    foreigns_lang = models.TextField(max_length=500, blank=True, default='Не заполнено')
    #Есть ли у вас опыт волонтерства? Если есть, то опишите его. Если нет - это не страшно)) *
    volonteer_exp = models.TextField(max_length=500, blank=True, default='Не заполнено')
    #Есть ли у вас опыт работы с детьми? Если есть, то опишите его *
    children_exp = models.TextField(max_length=500, blank=True, default='Не заполнено')
	#Какие дополнительные навыки могут быть полезны в сотрудничестве с Политехом? (возможно, вы прекрасно фотографируете или умеете красиво и профессионально говорить со сцены, напишите об этом!) *
    additional_skills = models.TextField(max_length=500, blank=True, default='Не заполнено')
    #Какие ожидания у вас от волонтерства в проектах Политехнического музея? Что волонтерство может дать лично вам?
    expectations = models.TextField(max_length=500, blank=True, default='Не заполнено')
    #Есть ли у Вас медицинские противопоказания, аллергия, в т.ч. на животных?
    allergy = models.TextField(max_length=500, blank=True, default='Не заполнено')
    #Согласие на обработку персональных данных в соответствие с Федеральным законом РФ от 27 июля 2006 года № 152-ФЗ «О персональных данных» *Если вы не даете согласия на обработку данных, то в соответствии с законом, все предоставленные вами данные будут немедленно удалены, и вы не будете внесены в список участников конференции *
    extended_profile = models.BooleanField(default=False)
    # ЭТА ХУИТА НЕ РАБОТАЕТ
    #profile_image = models.ImageField(upload_to = 'image_folder/', default = 'image_folder/None/no-img.jpg')


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
    reg_ending_at = models.DateTimeField()
    ending_at = models.DateTimeField()
    users_registered = models.CharField(max_length=10000, blank=True)
    min_karma = models.FloatField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Museum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=1200, blank=True, default='Не заполнено')
    image = models.ImageField(upload_to = 'images', default = 'images/no-img.jpg')
    members = models.TextField(max_length=500, blank=True, default='')

class MuseumMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    museum = models.IntegerField(blank=True)
    vorname = models.CharField(max_length=20, blank=True)
    nachname = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to = 'image_folder/', default = 'image_folder/None/no-img.jpg')