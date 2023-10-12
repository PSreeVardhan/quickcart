from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math

# Create your views here.
def index(request):
    allprods=[]
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}  
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        slides = math.ceil(n/4)
        allprods.append([prod,range(1,slides),slides])  
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("contact")
def tracker(request):
    return HttpResponse("tracker")
def search(request):
    return HttpResponse("search")
def productView(request):
    return HttpResponse("productview")
def checkout(request):
    return HttpResponse("checkout")