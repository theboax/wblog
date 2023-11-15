from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import User, UserProfile



class SignUpForm(UserCreationForm):

    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    phone_number = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),max_length=11,min_length=11)

    date_of_birth = forms.DateField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth YYYY-MM-DD'})
    )



class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2','phone_number')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number','bio','date_of_birth','email',)
