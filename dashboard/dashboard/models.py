from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. MFUMO WA USERS NA ROLES
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('salesman', 'Salesman'),
        ('readman', 'Readman'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='salesman')


# 2. BIASHARA YA M-PESA & NETWORKS
class MpesaTransaction(models.Transaction): # Ama Abstract Model/Model ya kawaida
    PROVIDER_CHOICES = (
        ('M-Pesa', 'M-Pesa'),
        ('Tigo Pesa', 'Tigo Pesa'),
        ('Airtel Money', 'Airtel Money'),
        ('HaloPesa', 'HaloPesa'),
    )
    provider = models.CharField(max_length=20, choices=PROVIDER_CHOICES)
    closing_cash = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    closing_e_float = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    commission_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    excess_or_shortage = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    transaction_date = models.DateTimeField(auto_now_add=True)
    salesman = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.provider} - {self.transaction_date.strftime('%Y-%m-%d')}"


# 3. BIASHARA YA SALUNI
class SalonTransaction(models.Model):
    service_name = models.CharField(max_length=100) # mf. Kusuka, Kunyoa
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2) # price - discount
    staff_name = models.CharField(max_length=100) # Kinyozi / Msusi
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_date = models.DateTimeField(auto_now_add=True)
    salesman = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.service_name} - TZS {self.net_amount}"


# 4. BIASHARA YA HOTSPOT INTERNET
class HotspotSale(models.Model):
    voucher_plan = models.CharField(max_length=50) # mf. Saa 1, Siku 1, Wiki 1
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
    salesman = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.voucher_plan} ({self.quantity}) - TZS {self.total_amount}"


class HotspotExpense(models.Model):
    title = models.CharField(max_length=100) # mf. Vocha/MB, Umeme, Starlink Bill
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.title} - TZS {self.amount}"
