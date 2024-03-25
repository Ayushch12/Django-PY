from django.shortcuts import render
from .models import Destination

# Create your views here.
# Define your view function


def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "This is my City"
    dest1.price = 700


    # Return an HTTP response with the text "Hello World"
    return render(request,'index.html',{'dest1': dest1})
