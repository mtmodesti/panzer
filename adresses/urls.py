from django.urls import path
from rest_framework_simplejwt import views as authview

from . import views

urlpatterns = {
  path("new/", views.CreateAddressView.as_view()),
  path("", views.ListAllAdressesView.as_view()),
  path("<address_id>/", views.RetrieveUpdateDestroyAddressView.as_view()),
}
