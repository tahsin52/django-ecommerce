from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse

from accounts.models import Account
from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('products_detail', args=[self.category.slug, self.slug])

    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])

        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])

        return count

    def __str__(self):
        return str(self.product_name)


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(varition_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(varition_category='size', is_active=True)


varition_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)


class Varition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    varition_category = models.CharField(max_length=155, choices=varition_category_choice)
    varition_value = models.CharField(max_length=155)
    is_active = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return str(self.varition_value)


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=155, blank=True)
    review = models.TextField(blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=50, blank=True)
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.subject)

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', blank=True)

    def __str__(self):
        return str(self.product.product_name)