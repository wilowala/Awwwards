from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from myapi.models import Profile, Rating, Post


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, label='',widget=forms.EmailInput(attrs={'class': 'form-control mb-4', 'placeholder': 'email'}))
    username =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4','placeholder': 'username'}))
    password1 = forms.CharField(max_length=200,label='',widget=forms.PasswordInput(attrs={'class': 'form-control mb-4', 'placeholder': 'password'}))
    password2 = forms.CharField(max_length=200, label='',widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','placeholder': 'confirm password'}))
    
    class Meta():
       model=User
       fields = ['email', 'username', 'password1', 'password2']

class SubmitForm(ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'description', 'image', 'post_url']
        

class RatingsForm(ModelForm):
    class Meta():
        model = Rating
        fields = ['design', 'usability', 'content']
        
class UpdateProfileForm(ModelForm):
    class Meta():
        model=Profile
        fields=['profile_photo', 'bio',]