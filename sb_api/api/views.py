from django.shortcuts import render
from django.views.generic import ListView

from .models import BackScratcher


class BackScratcherList(ListView):
    model = BackScratcher
