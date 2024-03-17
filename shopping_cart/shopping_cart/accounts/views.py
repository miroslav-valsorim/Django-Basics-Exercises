from django.contrib.auth import views as auth_views, authenticate, login, get_user_model, logout
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from shopping_cart.accounts.forms import CreateUserForm

# 'authenticate(request, **credentials)' -> returns the use if credentials match
# 'login(request, user)' -> attaches a cookie for the authenticated user

# The correct way to get the 'User' class
UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'

    # def get_success_url(self):
    #     return reverse('index')


class RegisterUserView(views.CreateView):
    # form_class = auth_forms.UserCreationForm
    form_class = CreateUserForm
    template_name = 'accounts/register_user.html'
    success_url = reverse_lazy('home_page')


# logout with FBV
def logout_view(request):
    logout(request)
    return redirect('home_page')


# logout with CBV
class CustomLogoutView(auth_views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            # Handle logout for POST request
            return super().dispatch(request, *args, **kwargs)
        else:
            logout(request)
            # Redirect to login page or any other desired URL for GET request
            return HttpResponseRedirect(reverse_lazy('index'))

# class LoginUserView(views.View):
#     form_class = auth_forms.AuthenticationForm
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': self.form_class()
#         }
#
#         return render(request, 'accounts/login_user.html', context)
#
#     def post(self, request, *args, **kwargs):
#         # form = self.form_class(request.POST or None)
#         # if form.is_valid():
#
#         username, password = request.POST['username'], request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         # print(user)
#
#         if user is not None:
#             # Add the user to the session
#             login(request, user)
#
#         return redirect('index')
