from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return HttpResponseRedirect("Posts/")