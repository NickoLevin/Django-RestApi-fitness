from dataclasses import fields
from .models import Trainers, Abonements, Clubs, Partners, Equipments, grouptraining
from django.forms import DateInput, DateTimeInput, ModelForm, NumberInput, TextInput, Textarea

class TrainersForm(ModelForm):
    class Meta:
        model = Trainers
        fields = ['name','surname','age','achivments']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя сотрудника'
            }),
             'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
                'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст сотрудника'
            }),
              'achivments': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Достижения сотрудника'
            }),
        }


class AbonementsForm(ModelForm):
    class Meta:
        model = Abonements
        fields = ['title','description','price']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название абонемента'
            }),
             'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание абонемента'
            }),
                'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
        }


class ClubsForm(ModelForm):
    class Meta:
        model = Clubs
        fields = ['club_name','location','workin_hours','date']

        widgets = {
            'club_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название клуба'
            }),
            'location': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Местонахождение'
            }),
             'workin_hours': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рабочие часы'
            }),
                'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата открытия'
            }),
        }


class PartnersForm(ModelForm):
    class Meta:
        model = Partners
        fields = ['organisation','product','contract']

        widgets = {
            'organisation': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование организации'
            }),
            'product': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Товар организации'
            }),
             'contract': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на сайт'
            }),
        }


class EquipmentsForm(ModelForm):
    class Meta:
        model = Equipments
        fields = ['equip','amount']

        widgets = {
            'equip': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название тренажера'
            }),
                'amount': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество в зале'
            }),
        }


class grouptrainingForm(ModelForm):
    class Meta:
        model = grouptraining
        fields = ['grouptraining','gr_description','personal','datetime']

        widgets = {
            'grouptraining': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тренировка'
            }),
            'gr_description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
             'personal': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тренер'
            }),
                'datetime': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время'
            }),
        }