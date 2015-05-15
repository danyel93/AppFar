from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	cuidad= forms.CharField(max_length=50)
	calle= forms.CharField(max_length=50)
	colonia= forms.CharField(max_length=50)
	telefono = forms.CharField(max_length=50)