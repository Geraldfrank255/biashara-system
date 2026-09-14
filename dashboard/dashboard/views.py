from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from .models import MpesaTransaction, SalonTransaction, HotspotSale, HotspotExpense

# 1. DASHBOARD YA ADMIN (Muhtasari wa Biashara Zote Tatu)
@login_required
def admin_dashboard(request):
    if request.user.role not in ['admin', 'readman']:
        return redirect('salesman_dashboard')

    today = timezone.now().date()

    # Sum za leo kwa M-Pesa
    mpesa_today = MpesaTransaction.objects.filter(transaction_date__date=today)
    total_mpesa_commission = mpesa_today.aggregate(Sum('commission_earned'))['commission_earned__sum'] or 0
    total_mpesa_shortage = mpesa_today.aggregate(Sum('excess_or_shortage'))['excess_or_shortage__sum'] or 0

    # Sum za leo kwa Saluni
    salon_today = SalonTransaction.objects.filter(service_date__date=today)
    total_salon_income = salon_today.aggregate(Sum('net_amount'))['net_amount__sum'] or 0
    total_salon_commission = salon_today.aggregate(Sum('commission_amount'))['commission_amount__sum'] or 0

    # Sum za leo kwa Hotspot
    hotspot_sales_today = HotspotSale.objects.filter(sale_date__date=today)
    total_hotspot_income = hotspot_sales_today.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    
    hotspot_expenses_today = HotspotExpense.objects.filter(expense_date__date=today)
    total_hotspot_expenses = hotspot_expenses_today.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'total_mpesa_commission': total_mpesa_commission,
        'total_mpesa_shortage': total_mpesa_shortage,
        'total_salon_income': total_salon_income,
        'total_salon_net_profit': total_salon_income - total_salon_commission,
        'total_hotspot_income': total_hotspot_income,
        'total_hotspot_net_profit': total_hotspot_income - total_hotspot_expenses,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)


# 2. SEHEMU YA MFANYAKAZI (Salesman Panel)
@login_required
def salesman_dashboard(request):
    return render(request, 'dashboard/salesman_form.html')
