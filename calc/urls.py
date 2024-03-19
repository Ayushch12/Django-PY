from django.urls import path
from django.contrib import admin
from . import views  # Import the views module

urlpatterns = [
    path('', views.home, name="home"),  # Define the path to the home view
    path("admin/", admin.site.urls),    # Optionally, include the admin URLs

]


