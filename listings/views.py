from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

# Home Page – All published listings
class PublishedListingList(generics.ListAPIView):
    queryset = Listing.objects.filter(is_published=True).order_by('-created_at')
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']  # sale or rent
    search_fields = ['title', 'description', 'address']

# Single Listing Detail View
class ListingDetail(generics.RetrieveAPIView):
    queryset = Listing.objects.filter(is_published=True)
    serializer_class = ListingSerializer
    lookup_field = 'id'  # Use ID in URL
    permission_classes = [AllowAny]

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingPurchaseView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            listing = Listing.objects.get(pk=pk, is_published=True, is_purchased=False)
            listing.is_purchased = True
            listing.purchased_by = request.user  # optional
            listing.save()
            return Response({"message": "Payment successful. Listing marked as purchased."}, status=status.HTTP_200_OK)
        except Listing.DoesNotExist:
            return Response({"error": "Listing not found or already purchased."}, status=status.HTTP_404_NOT_FOUND)