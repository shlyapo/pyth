from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordChangeDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.urls import path
from django.contrib import admin

from . import views
from .views import StartPageView, LoginView, RegistrationView, SignUpView

urlpatterns = [
    path('', StartPageView.as_view(), name='home'),
    path('register', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    #path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
]