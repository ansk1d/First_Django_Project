from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def root (request):
    return redirect("/blogs")

def new (request):
    return HttpResponse("placeholder to display a new form to create a new blog ")

def create (request):
    return redirect("/")

def number (request,num):
    return HttpResponse(f"placeholder to display blog number: {num}")

def edtnum (request,num):
    return HttpResponse(f"placeholder to edit blog {num}")

def destroy (request, num):
    return redirect("/blogs")