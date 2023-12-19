# authentication/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur',widget= forms.TextInput(attrs={'placeholder': 'Identifiant', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe', 'style': 'width: 300px;', 'class': 'form-control'}), label='Mot de passe')

class RegisterNewSensor(forms.Form):
    Numero_Machine = forms.DecimalField(label='Numero du capteur')
    ID_Capteur = forms.CharField(max_length=63, label='Identifiant du capteur Home Assistant',widget= forms.TextInput(attrs={'placeholder': 'Identifiant', 'style': 'width: 300px;', 'class': 'form-control'}))