from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import UserProfile
from .forms import StockAgreementForm, NDAForm

def register_with_invite(request, token):
    return redirect('login')

@login_required
def dashboard_redirect_view(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('/admin/')
    
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if profile.onboarding_completed:
        return redirect('qualified_dashboard')
    elif not profile.role_notes_acknowledged:
        return redirect('role_notes')
    elif not profile.stock_agreement_signed:
        return redirect('stock_agreement')
    else:
        return redirect('nda')

@login_required
def role_notes_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if profile.onboarding_completed:
        return redirect('qualified_dashboard')
        
    if request.method == 'POST':
        profile.role_notes_acknowledged = True
        profile.save()
        return redirect('stock_agreement')
    return render(request, 'evaluation/role_notes.html', {'profile': profile})

@login_required
def stock_agreement_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if profile.onboarding_completed:
        return redirect('qualified_dashboard')
    if not profile.role_notes_acknowledged:
        return redirect('role_notes')

    if request.method == 'POST':
        form = StockAgreementForm(request.POST, instance=profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.stock_agreement_signed = True
            instance.stock_signed_at = timezone.now()
            instance.save()
            return redirect('nda')
    else:
        form = StockAgreementForm(instance=profile)
    return render(request, 'evaluation/stock_agreement.html', {'form': form, 'profile': profile})

@login_required
def nda_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if profile.onboarding_completed:
        return redirect('qualified_dashboard')
    if not profile.stock_agreement_signed:
        return redirect('stock_agreement')

    if request.method == 'POST':
        form = NDAForm(request.POST, instance=profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.nda_signed_at = timezone.now()
            instance.onboarding_completed = True
            instance.save()
            return redirect('qualified_dashboard')
    else:
        form = NDAForm(instance=profile)
    return render(request, 'evaluation/nda.html', {'form': form, 'profile': profile})

@login_required
def qualified_dashboard_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'evaluation/qualified_dashboard.html', {'profile': profile})