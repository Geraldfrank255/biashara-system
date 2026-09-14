from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

def salesman_dashboard(request):
    return render(request, 'dashboard/salesman_form.html')
