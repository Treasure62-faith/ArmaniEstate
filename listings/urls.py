from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingPurchaseView, ListingViewSet, PublishedListingList, ListingDetail

router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')

urlpatterns = [
    path('listings/<int:pk>/purchase/', ListingPurchaseView.as_view(), name='listing-purchase'),  # 🛒 BEFORE router
    path('', include(router.urls)),  # 🔁 All ViewSet routes
    path('listings/', PublishedListingList.as_view(), name='listing-list'),
    path('listings/<int:id>/', ListingDetail.as_view(), name='listing-detail'),
]
