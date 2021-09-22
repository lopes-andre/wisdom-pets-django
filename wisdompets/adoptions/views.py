from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>Test home view</p>')

def pet_detail(request, pet_id):
    return HttpResponse('<h1>Test the pet detail view</h1>')