from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Postlar, Malumot

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(ListView):
    model = Malumot
    template_name = 'abaut.html'

class Listpage(ListView):
    model = Postlar
    template_name = 'list.html'