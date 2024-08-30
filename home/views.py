from django.shortcuts import render

# Create your views here.

def index(reqest):
    """ A view to return the index page"""
    return render(reqest, "home/index.html")
