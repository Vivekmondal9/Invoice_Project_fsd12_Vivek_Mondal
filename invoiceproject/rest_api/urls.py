from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import RegistrationView
urlpatterns=[
    path("users/register",csrf_exempt(RegistrationView.as_view()),name="Registration")
]