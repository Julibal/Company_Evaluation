from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'compensation', 'onboarding_completed', 'stock_agreement_signed')
    search_fields = ('userusername', 'useremail')
    fieldsets = (
        ('User & Status', {'fields': ('user', 'compensation', 'target_metric', 'onboarding_completed')}),
        ('Role & Target Briefing', {'fields': ('role_notes', 'role_notes_acknowledged')}),
        ('Stock Options Agreement', {'fields': ('stock_agreement_text', 'stock_agreement_signed', 'stock_signature_name', 'stock_signed_at')}),
        ('Non-Disclosure Agreement (NDA)', {'fields': ('nda_text', 'nda_signature_name', 'nda_signed_at')}),
    )