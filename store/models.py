from django.db import models
from django.urls import reverse

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
