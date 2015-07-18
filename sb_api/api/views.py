from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from .models import BackScratcher
from django.shortcuts import render

class BackScratcherList(ListView):
    model = BackScratcher


def Index(request):
    return render(request, 'api/index.html')
