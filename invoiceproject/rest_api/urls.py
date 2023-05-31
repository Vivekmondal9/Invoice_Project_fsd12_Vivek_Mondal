from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import RegistrationView,LoginView,InvoiceList,Itemadd,ItemwithId,NewItemAdd
urlpatterns=[
    path("users/register",csrf_exempt(RegistrationView.as_view()),name="Registration"),
    path("users/login",csrf_exempt(LoginView.as_view()),name="login"),
    path("invoices",InvoiceList.as_view(),name="invoice-list"),
    path("invoices/new",csrf_exempt(Itemadd.as_view()),name="item-add"),
    path("invoices/<int:invoice_id>",ItemwithId.as_view(),name="item-with-id"),
    path("invoices/<int:invoice_id>/items",csrf_exempt(NewItemAdd.as_view()),name="ner-item-add")

]