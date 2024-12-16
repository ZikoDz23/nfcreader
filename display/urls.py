from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan_card, name='scan_card'),  # Scan page
    path('card-info/<str:card_uid>/', views.card_info, name='card_info'),  # Show card info
    path('api/nfc/', views.nfc_data, name='nfc_data'),
]
