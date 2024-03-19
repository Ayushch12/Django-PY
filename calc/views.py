from django.shortcuts import render
from django.http import HttpResponse

# Define your view function
def home(request):
    # Return an HTTP response with the text "Hello World"
    return render(request,'home.html',{'name':'Ayush '})


def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2


    # Return an HTTP response
    return render(request,'result.html',{'result':res})


