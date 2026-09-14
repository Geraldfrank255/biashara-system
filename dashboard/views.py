from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@login_required
@user_passes_test(is_admin, login_url='/admin/login/')
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def salesman_dashboard(request):
    return render(request, 'dashboard/salesman_form.html')
