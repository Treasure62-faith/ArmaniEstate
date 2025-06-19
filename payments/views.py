from django.shortcuts import render
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import send_mail
from listings.models import Listing  # Make sure Listing model has a 'status' field like 'available', 'sold', etc.

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        metadata = intent.get('metadata', {})
        listing_id = metadata.get('listing_id')

        if listing_id:
            try:
                listing = Listing.objects.get(id=listing_id)
                listing.status = 'sold'  # Set your desired status
                listing.save()

                send_mail(
                    subject="Payment Confirmation",
                    message=f"Your payment for listing '{listing.title}' was successful!",
                    from_email="noreply@yourrealestate.com",
                    recipient_list=["olafarejoshua08@gmail.com"],  # Replace with user's email if available
                    fail_silently=False,
                )

                print(f"✅ Listing {listing_id} marked as sold & email sent.")

            except Listing.DoesNotExist:
                print("❌ Listing not found.")

    return HttpResponse(status=200)


class CreateCheckoutSessionView(APIView):
    def post(self, request):
        listing_id = request.data.get("listing_id")

        try:
            YOUR_DOMAIN = "http://127.0.0.1:8000"
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Listing Access',
                        },
                        'unit_amount': 5000,  # $50.00
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=f'{YOUR_DOMAIN}/success/',
                cancel_url=f'{YOUR_DOMAIN}/cancel/',
                metadata={
                    'listing_id': listing_id,
                    'user_id': request.user.id if request.user.is_authenticated else 'anonymous',
                },
            )

            return Response({
                'id': session.id,
                'url': session.url,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
