from django.urls import path
from .views import LoginView, ResgisterView, TestView

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("register/", ResgisterView.as_view()),
    path("getdata/", TestView.as_view()),
]
