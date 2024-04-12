from django.shortcuts import render
from django.http import HttpResponse
import logging

def index(request):
    return HttpResponse("<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. <br>Dolores ea itaque laboriosam neque nihil odio provident quis quo tempore vitae.</p>")


def about(request):
    return HttpResponse("about")