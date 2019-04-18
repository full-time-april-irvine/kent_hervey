
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    print("this is the second_django project, app:  firstappxxx")
    
    #return redirect("/")

    return HttpResponse("<h1>bbbthis is the second_django project, app:  firstapp</h2>")
    #return HttpResponse("<h1>this is in second project</h1><h2>this is the Shannon is very great equivalent of @app.route('/')!</h2>")

def some_method(request):
    print("this is the second_django project, app:  firstapp")

    return HttpResponse("<h1>placeholder to display a new form to create a new blog with a method named new</h2>")
    
    #return redirect("/")


def create(request):
    print("this is the second_django project, app:  firstapp, method is create")

    #return HttpResponse("<h1> create method placeholder to display a new form to create a new blog with a method named new</h2>")

    return redirect("/")


def show(request, my_val):
    print("printing " +my_val)
    return HttpResponse("<h3>placeholder to display blog number: " + my_val + " </h3>")

def edit(request, my_val):
    print("printing " +my_val)
    return HttpResponse("<h3>placeholder to edit blog: " + my_val + " </h3>")



def destroy(request, my_val):
    print("printing " +my_val)
    return redirect("/")