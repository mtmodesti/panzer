from django.urls import path

from . import views

urlpatterns = [
    path("newuser/", views.CreateUserView.as_view()),
    
]