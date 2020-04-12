from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about", views.About.as_view(), name="about"),
    path("post", views.Post.as_view(), name="post"),
    path("contact", views.Contact.as_view(), name="contact"),
]
