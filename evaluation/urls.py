from django.urls import path
from . import views

urlpatterns = [
    path('register/<uuid:token>/', views.register_with_invite, name='register_with_invite'),
    path('dashboard/', views.dashboard_redirect_view, name='dashboard_redirect'),
    path('dashboard/role-notes/', views.role_notes_view, name='role_notes'),
    path('dashboard/stock-agreement/', views.stock_agreement_view, name='stock_agreement'),
    path('dashboard/nda/', views.nda_view, name='nda'),
    path('dashboard/qualified/', views.qualified_dashboard_view, name='qualified_dashboard'),
]