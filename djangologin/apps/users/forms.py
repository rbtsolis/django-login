from django import forms
from .models import User


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username', 'password'
        )


# Esta es otra alternativa que puedes usar
"""
class LoginForm(forms.Form):

    username = forms,CharField(max_length=50)
    username = forms,CharField(max_length=50,
     widget = forms.TextInput( attrs = {
        'type' : 'password'
     }))
"""
