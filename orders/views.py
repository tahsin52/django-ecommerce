import datetime
import json

from django.shortcuts import render, redirect

from order_product.models import OrderProduct
from payment.models import Payment
from .models import Order
from carts.models import CartItem
from .forms import OrderForm


def payments(request):
    body = json.loads(request.body)
    print(body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])
    # Store transaction details in Payment model
    payment = Payment(
        user=request.user,
        payment_id=body['transactionID'],
        payment_moethod=body['payment_method'],
        amount_paid=order.total,
        status=body['status'],
    )
    payment.save()
    order.payment = payment
    order.is_ordered = True
    order.save()

    # Cart items to Order Product


    return render(request, 'orders/payments.html')


def place_order(request, total=0, quantity=0):
    current_user = request.user

    # if the cart count is less than or =0, then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (2 * total) / 100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing information inside
            order = Order()
            order.user = current_user
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.phone = form.cleaned_data['phone']
            order.email = form.cleaned_data['email']
            order.address_line_1 = form.cleaned_data['address_line_1']
            order.address_line_2 = form.cleaned_data['address_line_2']
            order.country = form.cleaned_data['country']
            order.city = form.cleaned_data['city']
            order.state = form.cleaned_data['state']
            order.order_note = form.cleaned_data['order_note']

            # Get user ip in django
            order.ip = request.META.get('REMOTE_ADDR')

            order.order_total = grand_total
            order.tax = tax

            order.save()
            # Generate order number

            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)

            current_date = d.strftime("%Y%m%d")  # 20210525
            order_number = current_date + str(order.id)
            order.order_number = order_number

            order.save()

            order = Order.objects.get(user=request.user, is_ordered=False, order_number=order_number)

            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total
            }

            return render(request, 'orders/payments.html', context)

    else:
        return redirect('checkout')
