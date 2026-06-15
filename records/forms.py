from django import forms
from django.utils import timezone
from .models import Darta, Chalan
from django.contrib.auth.models import User


class DartaForm(forms.ModelForm):

    darta_date = forms.DateField(
        initial=timezone.now().date,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Darta
        exclude = ['created_by']


class ChalanForm(forms.ModelForm):

    chalan_date = forms.DateField(
        initial=timezone.now().date,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Chalan
        exclude = ['created_by']


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False
    )

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'is_staff'
        ]