from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView

from .forms import LoginForm


class LoginView(FormView):

    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/login/'

    def form_valid(self, form):

        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

        print(user)

        if user is not None and user.is_active:
            login(self.request, user)
        return super(LoginView, self).form_valid(form)


def Logout(request):
    logout(request)
    return redirect('/')
