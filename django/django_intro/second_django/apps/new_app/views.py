from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print("project second_django, new_app")
    return HttpResponse("<h1>Hello World from </h1><h2>project second_django, new_app</h2>")
    
