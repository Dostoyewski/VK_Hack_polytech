from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ChangeForm(forms.Form):
    # ЭТА ХУИТА НЕ РАБОТАЕТ
    #profile_image = forms.ImageField(label="Аватар")
    vorname = forms.CharField(max_length=20, label='Имя')
    nachname = forms.CharField(max_length=50, label='Фамилия')
    bio = forms.CharField(max_length=500, label='Статус')
    location = forms.CharField(max_length=30, label='Город')
    birth_date = forms.DateField(label='Дата рождения')
    urlVK = forms.CharField(max_length=100, label='Ссылка на профиль ВК')
    phone = PhoneNumberField(label='Контактный телефон')
    #Место учебы/работы
    work_place = forms.CharField(max_length=500, label='Место учебы/работы')
    #Специальность по диплому  
    specialization = forms.CharField(max_length=500, label='Специальность по диплому')
    #Какими иностранными языками Вы владеете (укажите уровень владения)? *
    foreigns_lang = forms.CharField(max_length=500, label='Какими иностранными языками Вы владеете (укажите уровень владения)? *')
    #Есть ли у вас опыт волонтерства? Если есть, то опишите его. Если нет - это не страшно)) *
    volonteer_exp = forms.CharField(max_length=500, label='Есть ли у вас опыт волонтерства? Если есть, то опишите его. Если нет - это не страшно)) *')
    #Есть ли у вас опыт работы с детьми? Если есть, то опишите его *
    children_exp = forms.CharField(max_length=500, label='Есть ли у вас опыт работы с детьми? Если есть, то опишите его *')
    additional_skills = forms.CharField(max_length=500, label='Какие дополнительные навыки могут быть полезны в сотрудничестве с Политехом? (возможно, вы прекрасно фотографируете или умеете красиво и профессионально говорить со сцены, напишите об этом!)')
    expectations = forms.CharField(max_length=500, label='Какие ожидания у вас от волонтерства в проектах Политехнического музея? Что волонтерство может дать лично вам?')
    allergy = forms.CharField(max_length=500, label='Есть ли у Вас медицинские противопоказания, аллергия, в т.ч. на животных?')
    

class CommentForm(forms.Form):
    ball = forms.IntegerField(max_value=10, min_value=0, label='Оцените деятельность волонтера по шкале от 0 до 10')
    comment = forms.CharField(max_length=200, label='Комментарий')
    phone = PhoneNumberField(label='Телефон для верификации комментария')

class RegCommentForm(forms.Form):
    ball = forms.IntegerField(max_value=10, min_value=0, label='Оцените деятельность волонтера по шкале от 0 до 10')
    comment = forms.CharField(max_length=200, label='Комментарий')


class ApproveForm(forms.Form):
    code = forms.IntegerField(min_value=1000, max_value=9999, label='Введите SMS-код')