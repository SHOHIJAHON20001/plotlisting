from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def listings(request):
    return render(request, 'listing.html')

def contact(request):
    return render(request, 'contact.html')