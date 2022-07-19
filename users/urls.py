from django.urls import path
from rest_framework_simplejwt import views as authview

from . import views

urlpatterns = [
    path("login/", authview.TokenObtainPairView.as_view()),
    path("", views.ListUsersView.as_view()),
    path("register/", views.CreateUserView.as_view()),
    path("<user_id>/", views.RetrieveUpdateDestroyUserView.as_view()),
]
