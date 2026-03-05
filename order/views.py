from django.shortcuts import render
from order.models import Basket, BasketItem
from product.models import Product
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
# Create your views here.


# def update_item(request):
#     print("USER:", request.user)
#     print("AUTH:", request.user.is_authenticated)
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print(productId)
#     print(action)

#     product = Product.objects.get(id = productId)

#     basket, created = Basket.objects.get_or_create(user = request.user, is_active = True)
#     basketItem, created = BasketItem.objects.get_or_create(basket = basket, product = product)

#     if action == 'add':
#         if created:
#             basketItem.quantity = 1
#         else:
#             basketItem.quantity += 1

#     if action == 'remove':
#         basketItem.quantity -= 1

#     basketItem.save()

#     if basketItem.quantity <= 0:
#         basketItem.delete()

#     return JsonResponse('Item was added!', safe=False)


@require_POST
def update_item(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'login required'}, status=401)

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    product = Product.objects.get(id=productId)

    basket, created = Basket.objects.get_or_create(
        user=request.user,
        is_active=True
    )

    basketItem, created = BasketItem.objects.get_or_create(
        basket=basket,
        product=product
    )

    if action == 'add':
        basketItem.quantity = basketItem.quantity + 1 if not created else 1

    if action == 'remove':
        basketItem.quantity -= 1

    basketItem.save()

    if basketItem.quantity <= 0:
        basketItem.delete()

    return JsonResponse({'status': 'ok'})



def cart(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user, is_active=True).prefetch_related('items__product').first()
    else:
        basket = None
    context = {
        'basket' : basket
    }
    return render(request, 'cart.html', context)


def checkout(request):
    return render(request, 'checkout.html')


def emptycart(request):
    return render(request, 'empty-cart.html')
