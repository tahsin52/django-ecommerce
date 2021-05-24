from django.db import models

from accounts.models import Account


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=155)
    payment_method = models.CharField(max_length=155)
    amount_paid = models.CharField(max_length=155)
    status = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.payment_id)
