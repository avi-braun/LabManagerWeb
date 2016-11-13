from django import forms
from .models import User

class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    to=forms.EmailField()
    comment=forms.CharField(required=False,widget=forms.Textarea)

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('name','email','user_rank')
