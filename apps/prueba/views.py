from django.shortcuts import render

#importing the most basic class based view
from django.views.generic import TemplateView
# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home.html'