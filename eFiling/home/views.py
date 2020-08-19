from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request


def home(request):
    return render(request, 'Index.html')
