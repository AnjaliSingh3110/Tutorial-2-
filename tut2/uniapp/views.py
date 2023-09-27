# uniapp/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
  template_name = 'home.html'

class ProfilePageView(TemplateView):
  template_name = 'profile.html'

class ModulePageView(TemplateView):
  template_name = 'module.html'

# Create your views here.
