from django.shortcuts import render

# Create your views here.
# Define your view function
def index(request):
    # Return an HTTP response with the text "Hello World"
    return render(request,'index.html')
