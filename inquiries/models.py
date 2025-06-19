from django.db import models
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()

class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry by {self.user.username} on {self.listing.title}"
