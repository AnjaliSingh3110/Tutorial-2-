# uniapp/urls.py 
from django.urls import path 
from .views import HomePageView, ProfilePageView, ModulePageView

urlpatterns = [
  path('module/', ModulePageView.as_view(), name='module'),
  path('profile/', ProfilePageView.as_view(), name='profile'),
  path('', HomePageView.as_view(), name='home'),
  ]