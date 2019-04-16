
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("<h2>this is the Shannon is helpful of @app.route('/')!</h2>")