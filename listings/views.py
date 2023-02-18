from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing

def get_listings(request):
    if request.method == 'GET':
        listings = Listing.objects.all()
        print('this out:', request.GET['name'])
        return HttpResponse(listings.first().address)
    else:
        return
