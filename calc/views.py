from django.shortcuts import render
from django.http import HttpResponse

# Define your view function
def home(request):
    # Return an HTTP response with the text "Hello World"
    return render(request,'home.html',{'name':'Ayush '})

