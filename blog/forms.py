from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ChangeForm(forms.Form):
    vorname = forms.CharField(max_length=20, label='Имя')
    nachname = forms.CharField(max_length=50, label='Фамилия')
    bio = forms.CharField(max_length=500, label='Статус')
    location = forms.CharField(max_length=30, label='Город')
    birth_date = forms.DateField(label='Дата рождения')
    urlVK = forms.CharField(max_length=100, label='Ссылка на профиль ВК')
    phone = PhoneNumberField(label='Контактный телефон')

class CommentForm(forms.Form):
    vorname = forms.CharField(max_length=20, label='Имя')
    nachname = forms.CharField(max_length=50, label='Фамилия')
    ball = forms.IntegerField(max_value=10, min_value=0)
    comment = forms.CharField(max_length=200, label='Комментарий')
    phone = PhoneNumberField(label='Телефон для верификации комментария')

class ApproveForm(forms.Form):
    code = forms.IntegerField(min_value=1000, max_value=9999, label='Введите SMS-код')