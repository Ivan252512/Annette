from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "main/index.html"

class About(TemplateView):
    template_name = "main/about.html"

class Post(TemplateView):
    template_name = "main/post.html"

class Contact(TemplateView):
    template_name = "main/contact.html"


# Create your views here.
