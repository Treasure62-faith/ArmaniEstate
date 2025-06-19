from django.urls import path
from .views import InquiryCreateView

urlpatterns = [
    path('send/', InquiryCreateView.as_view(), name='send-inquiry'),
]
