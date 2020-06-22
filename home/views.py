from django.shortcuts import render, get_object_or_404, redirect
from .forms import StartForm

# Create your views here.
def home_page(request):
    return render(request, 'home.html')