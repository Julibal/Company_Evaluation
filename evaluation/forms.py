from django import forms
from .models import UserProfile

class StockAgreementForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['stock_signature_name']
        widgets = {
            'stock_signature_name': forms.TextInput(attrs={
                'class': 'w-full bg-slate-950/60 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-cyan-500',
                'placeholder': 'Type your full legal name to sign'
            })
        }

class NDAForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nda_signature_name']
        widgets = {
            'nda_signature_name': forms.TextInput(attrs={
                'class': 'w-full bg-slate-950/60 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-emerald-500',
                'placeholder': 'Type your full legal name to sign'
            })
        }