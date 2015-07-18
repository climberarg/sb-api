from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from .models import BackScratcher


class BackScratcherList(ListView):
    model = BackScratcher


def Index(request):
    return HttpResponse('Are we alone in the universe?')
