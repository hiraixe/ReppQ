from django.urls import path
from . import views
from .views import materials, request_quote
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('request/', views.request_quotation, name='request_quotation'),
    path('quotations/', views.quotation_list, name='quotation_list'),
    path('quotation/<int:pk>/', views.quotation_detail, name='quotation_detail'),
    path('register/', views.register, name='register'),  # Route for user registration
    path('login/', LoginView.as_view(template_name='quotes/login.html'), name='login'),  # Route for user login
    path('logout/', LogoutView.as_view(), name='logout'),  # Route for user logout
    path('quotes/', views.dashboard, name='dashboard'),  # Route for dashboard
    path('project/<int:project_id>/materials/', materials, name='materials'),
    path('request-quote/', views.request_quote, name='request_quote'),
    path('submit-quotation/', views.submit_quotation, name='submit_quotation'),
    ]