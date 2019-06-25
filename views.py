from django.http import HttpResponse


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import proucts

def index(request):
    product = Product.objects.all()
    return render('request', 'index.htm', {'products': product})

#we need to tell django that if there is a request /products, call -> index. we need to map the urls to the index function

def new(request):
    return Httpresponse('New Products')


