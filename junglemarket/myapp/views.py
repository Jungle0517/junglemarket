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

def detail(request, id=None):
    #return HttpResponse(id)
    product = ProductModel.objects.get(id = id)
    return render(request, 'detail.html', locals())

def addtocart(request, type=None, id=None):
    global cartlist
    # add update empty remove
    if type =='add':
        product = ProductModel.objects.get(id = id)

        noCartsession = True
        if noCartSession:
            templist = []
            #(pname, pprice, 1, 1*pprice)
            templist.append(product.pname)
            templist.append(str(product.pprice))
            templist.append(str(1))
            templist.append(str(product.pprice*1))
            cartlist.append(templist)
            request.session['cartlist'] = cartlist
            return HttpResponse('已選購商品')


#def set_cookie(request, key=None, value=None):
    #response = HttpResponse('Cookie OK')
    #response.set_cookie(key, value)
    #return response

#def set_session(request, key=None, value=None):
    #response = HttpResponse('Session OK')
    #request.session[key] = value
    #return response