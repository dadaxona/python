from django.urls import path
from .views import HomePageView, AboutPageView, Listpage

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('list/', Listpage.as_view(), name='list')

]