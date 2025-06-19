from django.db import models

class Listing(models.Model):
    CATEGORY_CHOICES = (
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='listing_images/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
