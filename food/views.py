from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def birayani(request):
    return HttpResponse('birayani is tasty')
    
def aalu(request):
    return render(request,'food.html')