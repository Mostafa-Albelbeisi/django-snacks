from django.shortcuts import render
from django .views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home_page.html'


class AboutPage(TemplateView):
    template_name='about.html'

