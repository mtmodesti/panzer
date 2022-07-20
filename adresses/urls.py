from django.urls import path
from rest_framework_simplejwt import views as authview

from . import views

urlpatterns = {
  # path("<user_id>/", views.RetrieveUpdateDestroyAddressUserView.as_view()),
   path("new/", views.ListAllAddressView.as_view())
}