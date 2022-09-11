from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from allauth.account.forms import LoginForm




class UserRegisterform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','year','bio','image']
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Name"
        self.fields["bio"].label = "Bio"
        self.fields["year"].label = "Year"
        self.fields["image"].label = ""




class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"].label = ""
        self.fields["password"].label = ""


