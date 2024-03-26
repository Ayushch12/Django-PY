from django.shortcuts import render
from .models import Destination

# Create your views here.
# Define your view function


def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "This is my City"
    dest1.price = 700
    dest1.img = "destination_1.jpg"
    dest1.offer = False


    dest2 = Destination()
    dest2.name = "India"
    dest2.desc = "Nulla pretium tincidunt felis, nec."
    dest2.price = 1000
    dest2.img = "destination_2.jpg"
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "Nepal"
    dest3.desc = "Nulla pretium tincidunt felis, nec."
    dest3.price = 12000
    dest3.img = "destination_3.jpg"
    dest3.offer = False

    dests = [dest1, dest2, dest3]


    # Return an HTTP response with the text "Hello World"
    return render(request,'index.html',{'dests': dests})
