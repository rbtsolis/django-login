from django import forms


# Este es el formulario de Login
class LoginForm(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'password'}))
