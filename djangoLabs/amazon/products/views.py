from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
	return render(request, 'products/nav.html')

def home(request):
	mylist = ["Mohamed", "Ali", "Yara", "Sami", "Noha", "Adel", "Aya"]
	context = {'mylist':mylist}
	return render(request, 'products/home.html', context)	


def contact(request):
	return render(request, 'products/contact.html')


def about(request):
	return render(request, 'products/about.html')
