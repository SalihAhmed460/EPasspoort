import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
        )
        return JsonResponse({'client_secret': payment_intent.client_secret})
    return JsonResponse({'error': 'Invalid request method'}, status=400)