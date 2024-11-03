# accounts/urls.py

from django.urls import path
from .views import home, login_view

urlpatterns = [
    path('', home, name='home'),  # Root URL for the accounts app
    path('login/', login_view, name='login'),  # URL for the login view
]