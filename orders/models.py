from django.db import models

from accounts.models import Account
from payment.models import Payment


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=55)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=155)
    address_line_1 = models.CharField(max_length=155)
    address_line_2 = models.CharField(max_length=155, blank=True)
    country = models.CharField(max_length=155)
    state = models.CharField(max_length=155)
    city = models.CharField(max_length=155)
    order_note = models.CharField(max_length=355, blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=155, choices=STATUS, default='New')
    ip = models.CharField(max_length=25, blank=True)
    is_ordered = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)