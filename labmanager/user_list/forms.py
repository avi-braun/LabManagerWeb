from django import forms
from .models import User
from django.utils.translation import ugettext_lazy as _


class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    to=forms.EmailField()
    comment=forms.CharField(required=False,widget=forms.Textarea)

class Add_userForm(forms.ModelForm):
    class Meta:
        model=User
        # fields=('name','email','supervisor','user_type','user_rank','status','CID','join_date')
        fields = '__all__'

        help_texts = {
            'name': _('*'),
            'email': _('*'),
            'supervisor': _('*'),
            'user_type': _('*'),
            'user_rank': _('*'),
            'status': _('*'),
            'join_date': _('*'),

        }
        error_messages = {
            'name': {
                'max_length': _("This users's name is too long."),
            },
        }