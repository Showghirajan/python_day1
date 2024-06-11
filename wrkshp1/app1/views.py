from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



   # return n1*n1
def fact(f1): 
    f1=1
    for i in range(1,10):
        f1=f1*i
        return HttpResponse("factorial is:".f1)
    

       