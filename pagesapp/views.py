from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Postlar
from django.urls import reverse_lazy
# Create your views here.
class HomePageView(ListView):
    model = Postlar
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Postlar
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Postlar
    template_name = 'post_new.html'
    fields = ['title','author','body']

class BlogUpdateView(UpdateView):
    model = Postlar
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Postlar
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

