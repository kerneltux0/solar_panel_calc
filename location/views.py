from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def locateUser(request):
    context = {}
    return render(request, 'location.html', context)