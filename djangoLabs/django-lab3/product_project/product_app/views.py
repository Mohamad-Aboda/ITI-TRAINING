from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product, Category
# Create your views here.

products = [
    {"name":"tea", "img":"tea.jpeg"}, 
    {"name":"chicken", "img":"chicken.jpeg"}, 
    {"name":"Meat", "img":"meat.jpeg"}, 
    {"name":"orange", "img":"orange.jpeg"},
    {"name":"mango", "img":"mango.jpeg"}, 
    {"name":"tomato", "img":"tomato.jpeg"}, 
    {"name":"potato", "img":"potato.jpeg"}

]
def home(request):
    database_products = Product.objects.all()
    context = {"products":products, 'database_products':database_products}
    
    return render(request, 'product_app/home.html', context)


def about(request):
    return render(request, 'product_app/about.html')


def contact(request):
    return render(request, 'product_app/contact.html')

    



def index(request):
    return render(request, 'product_app/base.html')



def add(request):
    if request.method == "GET":
        return render(request, "product_app/add.html")

    if request.method == "POST":
        prod = Product(name = request.POST["name"], img = request.POST["img"])
        # category = Category.objects.filter(request.POST["category"]))
        prod.save()
        # prod = Product()
        # prod.name = request.POST["name"]
        # prod.img = request.POST["img"]
        # mycategory = Category.objects.get(request.POST["Categorys"])
        # prod.category = mycategory
        
        return redirect('home')


def added(request):
    return render(request, "product_app/added.html")


def search(request):
    if request.method == "GET":
        print("hi and welcome ")
    if request.method == "POST":
        searchname = request.POST["search"]
        products = Product.objects.filter(name=searchname)
        context = {"searchres":products}
        return render(request, 'product_app/search.html', context)
    elif request.method == "GET":
        return render(request, 'product_app/search.html')



def delete(request):
    if request.method == "GET":
        return render(request, "product_app/delete.html")
    if request.method == "POST":

        print(request.POST["search"])
        prod = Product.objects.filter(name=request.POST["search"])
        prod.delete()
        # return render(request, "product_app/home.html")
        return redirect('home')





def update(request):
    return render(request, "product_app/update.html")
