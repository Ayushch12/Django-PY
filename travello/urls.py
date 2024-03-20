from django.urls import path
from django.contrib import admin
from . import views  # Import the views module

urlpatterns = [
    path('', views.index, name="index"),  # Define the path to the home view
    # path('add',views.add, name ='add' )

]
