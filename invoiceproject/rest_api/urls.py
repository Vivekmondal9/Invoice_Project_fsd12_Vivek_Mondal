from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import RegistrationView,LoginView
urlpatterns=[
    path("users/register",csrf_exempt(RegistrationView.as_view()),name="Registration"),
    path("users/login",csrf_exempt(LoginView.as_view()),name="login")
]