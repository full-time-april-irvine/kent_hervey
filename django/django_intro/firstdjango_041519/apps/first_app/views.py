
from django.shortcuts import render, HttpResponse
def index(request):
    print("first project, first app")
    #return HttpResponse("<h2>this is the Shannon is helpful of @app.route('/')!</h2>")
    return HttpResponse("<h2>This is the first_app in project:  firstdjango_041519</h2><p>8</p>")