
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import store, product_detail, search, submit_review

urlpatterns = [
    path('', store, name='store'),
    path('category/<slug:category_slug>/', store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', product_detail, name='products_detail'),
    path('search/', search, name='search'),
    path('submit_review/<int:product_id>/', submit_review, name='submit_review')
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
