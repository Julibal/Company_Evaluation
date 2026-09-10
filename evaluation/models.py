from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    compensation = models.CharField(max_length=255, default="Standard Package")
    target_metric = models.CharField(max_length=255, blank=True, null=True)
    
    role_notes = models.TextField(default="Review your assigned role and target goals.")
    role_notes_acknowledged = models.BooleanField(default=False)
    
    stock_agreement_text = models.TextField(default="In consideration of your engagement, you are granted stock options as outlined by corporate policy.")
    stock_agreement_signed = models.BooleanField(default=False)
    stock_signature_name = models.CharField(max_length=255, blank=True, null=True)
    stock_signed_at = models.DateTimeField(blank=True, null=True)
    
    nda_text = models.TextField(default="In consideration of your engagement with the company, you agree to protect and keep confidential all proprietary information, trade secrets, source code, financial models, and customer lists.")
    nda_signature_name = models.CharField(max_length=255, blank=True, null=True)
    nda_signed_at = models.DateTimeField(blank=True, null=True)
    
    onboarding_completed = models.BooleanField(default=False)

    def str(self):
        return f"{self.user.username} Profile"