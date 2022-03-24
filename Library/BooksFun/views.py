from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'BooksFun/index.html')

def about(request):
    return render(request, 'BooksFun/about.html')

def top(request):
    return render(request, 'BooksFun/top.html')

def reminder(request):
    return render(request, 'BooksFun/reminder.html')