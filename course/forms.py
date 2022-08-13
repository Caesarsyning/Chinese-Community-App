from django import forms
from django.forms import Textarea, TextInput
from django.contrib.auth.models import User
from . import models

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

