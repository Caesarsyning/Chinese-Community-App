from django import forms
from django.forms import Textarea, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
from allauth.account.forms import LoginForm






class CommentCreationForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'placeholder': 'Type comment...','rows':2}),
        }
    def __init__(self, *args, **kwargs):
        super(CommentCreationForm, self).__init__(*args, **kwargs)
        self.fields["content"].label = ""


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['name','year','bio','image']
#     def __init__(self, *args, **kwargs):
#         super(ProfileUpdateForm, self).__init__(*args, **kwargs)
#         self.fields["name"].label = "Name"
#         self.fields["bio"].label = "Bio"
#         self.fields["year"].label = "Year"
#         self.fields["image"].label = ""



