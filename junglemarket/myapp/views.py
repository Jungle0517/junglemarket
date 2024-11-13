from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import ProductModel

# Create your views here.

def index(request):
    #name = 'jungle'
    #return HttpResponse('index')

    products = ProductModel.objects.all()
    #print(products)
    productlist = []
    for i in range(1,3):
        product = ProductModel.objects.get(id = i)
        productlist.append(product)
    return render(request, 'index.html', locals())