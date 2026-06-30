from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    suburb = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, default="NT")
    postcode = models.CharField(max_length=10, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name