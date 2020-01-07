from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'shop/index.html')

def about(request):
  return render(request, 'shop/about.html')

def contact(request):
  return HttpResponse("We are at Contact")

def tracker(request):
  return HttpResponse("We are at tracker")

def search(request):
  return HttpResponse("We are at search")

def productView(request):
  return HttpResponse("We are at product view")

def checkout(request):
  return HttpResponse("We are at checkout")