from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def top(request) -> render:
    return render(request, 'login/top.html')
