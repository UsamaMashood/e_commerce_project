from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def shop_home(request):
    prod = Product.objects.values('catagory')
    allprod = []
    cats = {item['catagory'] for item in prod}
    print(type(cats))
    for cat in cats:
        products = Product.objects.filter(catagory = cat)
        nSlides = ceil(len(products)/4)
        allprod.append([products, nSlides, range(1,nSlides)])
    return render(request, 'shop/home.html', {'params' : allprod})

def productview(request,pd_id):
    product = get_object_or_404(Product,pk = pd_id)


    return render(request,'shop/view.html', {'product' : product})


def shop_contect(request):
    return HttpResponse('shop contect')

def shop_about(request):
    return HttpResponse('shop about')

def tracker(request):
    return HttpResponse('shop tracker')

def search(request):
    return HttpResponse('shop search')


def checkout(request):
    return HttpResponse('shop checkout')