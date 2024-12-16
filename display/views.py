from django.shortcuts import render, redirect
from .models import NationalID
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def scan_card(request):
    # This is the view that asks for NFC card scan
    return render(request, 'scan_card.html')

def card_info(request, card_uid):
    try:
        card = NationalID.objects.get(card_uid=card_uid)
        return render(request, 'display_info.html', {'card': card})
    except NationalID.DoesNotExist:
        return render(request, 'error.html', {'message': 'Card not found.'})



@csrf_exempt  # Disabling CSRF for simplicity in this example (use with caution)
def nfc_data(request):
    if request.method == 'POST':
        # Get the UID from the request
        card_uid = request.POST.get('card_uid')
        
        # Find the corresponding card info in the database
        try:
            card = NationalID.objects.get(card_uid=card_uid)
            # Return the card information as a JSON response
            return JsonResponse({
                'full_name': card.full_name,
                'date_of_birth': card.date_of_birth,
                'id_number': card.id_number,
                'address': card.address,
            })
        except NationalID.DoesNotExist:
            return JsonResponse({'error': 'Card not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request.'}, status=400)
