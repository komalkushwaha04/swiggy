from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def icecream(request):
    return HttpResponse('icecream is tasty')

def puri(request):
    return render(request,'instamart.html')