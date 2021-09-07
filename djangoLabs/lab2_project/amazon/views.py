from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


students = [
    {"name": "Ahmed", "img": "1.jpeg"},
    {"name": "Mohamed", "img": "2.jpeg"},
    {"name": "Ali", "img": "3.jpeg"},
    {"name": "Noha", "img": "4.jpeg"},
    {"name": "omar", "img": "5.jpeg"},
    {"name": "yara", "img": "6.jpeg"}, 
    {"name": "sami", "img": "7.jpeg"}, 
    {"name": "mai", "img": "8.jpeg"}, 
    {"name": "Khaled", "img": "9.jpeg"}
]

def home(request):
    context = {"students":students}
    return render(request, 'amazon/home.html', context)

def about(request):
    return render(request, 'amazon/about.html')

def contact(request):
    return render(request, 'amazon/contact.html')


def details(request, std_name):
     
    student = {}
    for std in students:
        if std["name"] == std_name:
             student = std

    context = {"student": student}
     # return HttpResponse(std_name)
    return render(request, "amazon/details.html/",context)
