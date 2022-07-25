from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .api import Reminder

def index(request):
    return render(request, 'reminder/index.html')

def make(request):
    data = request.POST
    print(data)
    Reminder.create(title=data["title"])