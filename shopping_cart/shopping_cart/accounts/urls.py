from django.urls import path

from shopping_cart.accounts.views import LoginUserView, RegisterUserView, logout_view, CustomLogoutView

urlpatterns = (
    path("login/", LoginUserView.as_view(), name="login-user"),
    path('register/', RegisterUserView.as_view(), name="register-user"),
    path('logout/', logout_view, name='logout-user'),
    path('customlogout/', CustomLogoutView.as_view(), name='custom-logout'),
)