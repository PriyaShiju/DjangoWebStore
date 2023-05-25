from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse
from Store.models import Product

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def welcome(request):    
    return render(request,"Welcome.html", {"productscount":Product.objects.count(),
                                                 "products": Product.objects.all(),
                                                 "x":"https://github.com/PriyaShiju?tab=repositories"})
def ProductDetail(request,id):
    p=Product.objects.get(pk=id) 
    #p=Product.objects.all() #.filter(pk=4)
    #p = get_object_or_404(Product, pk=id)
    return render(request,"ProductDetail.html" , {'p':p })
    

def ProductView():
    return HttpResponse( Product.objects.count())

def CategoryView(request): #name
    #p=Product.objects.filter(categories__categoryName=name)    
    
    return render(request,"Category.html" , {'products':Product.objects.all() })
