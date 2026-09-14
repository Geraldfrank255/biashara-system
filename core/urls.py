from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('sales/', views.salesman_dashboard, name='salesman_dashboard'),
]
