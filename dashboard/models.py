from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('salesman', 'Salesman'),
    )
    BUSINESS_CHOICES = (
        ('mpesa', 'M-Pesa'),
        ('salon', 'Salon'),
        ('hotspot', 'Hotspot'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='salesman')
    business_assigned = models.CharField(max_length=10, choices=BUSINESS_CHOICES, null=True, blank=True)

class MpesaTransaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class SalonService(models.Model):
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class HotspotVoucher(models.Model):
    code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
