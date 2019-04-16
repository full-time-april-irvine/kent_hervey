
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the exquivalent of @app.route('/')!")