from django.urls import path, include
from django.contrib import admin
from calc import views  # Import the views module

urlpatterns = [
    path("", views.home, name="home"),  # Define the path to the home view
    path("admin/", admin.site.urls),    # Optionally, include the admin URLs
    path("calc/", include("calc.urls")), # Include URLs from the calc app
]
