from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Product

#This will define and render the page in the index.html page
def index(request):

    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'products/index.html', context)
	
@csrf_exempt
def getProduct(request, id):
    if request.method == "GET":
        prod = Product.objects.get(id=id)
        getProd = {}
        getProd['id'] = prod.id
        getProd['name'] = prod.name
        getProd['desc'] = prod.description
        getProd['price'] = prod.price
        return JsonResponse(getProd)

@csrf_exempt
def addProduct(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        price = request.POST.get('price', '')
        newProdList = Product(name=name, description=description, price=price)
        newProdList.save()
        changeToJson = {
            'id': newProdList.id,
            'name': name,
        }
        return JsonResponse(changeToJson)

@csrf_exempt
def deleteProduct(request, id):
    if request.method == "DELETE":
        chosenProdList = Product.objects.get(id=id)
        chosenProdList.delete()
        return HttpResponse("Product deleted!")

@csrf_exempt
def updateProduct(request, id):
    if request.method == "PUT":
        prodList = Product.objects.get(id=id)
        put = QueryDict(request.body)
        prodList.name = put.get('name')
        prodList.description = put.get('description')
        prodList.price = put.get('price')
        prodList.save()
        changeToJson = {
            'id': prodList.id,
            'name': prodList.name,
        }
        return JsonResponse(changeToJson)
