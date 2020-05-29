from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from user.models import Account

class RegistrationForm(UserCreationForm):
	email=forms.EmailField(max_length=255,help_text='required enter email id')

	class Meta:
		model=Account
		fields=('email','username','semester','password1','password2','semester')
class AccountForm(forms.ModelForm):
	password=forms.CharField(label='Password',widget=forms.PasswordInput)
	class Meta:
		model=Account
		fields=('email','password')

	def clean(self):
		email=self.cleaned_data['email']
		password=self.cleaned_data['password']
		if not authenticate(email=email,password=password):
			return forms.ValidationError('not authenticate user')
