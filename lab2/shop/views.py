from django.db.models import Q
from django.shortcuts import render

from .models import Cart


def carts_list(request):
    carts = Cart.objects.select_related('customer').prefetch_related('products')

    search = request.GET.get('search', '').strip()
    status = request.GET.get('status', '')

    if search:
        carts = carts.filter(
            Q(customer__name__icontains=search) |
            Q(customer__email__icontains=search)
        )

    if status:
        carts = carts.filter(status=status)

    context = {
        'carts': carts,
        'search': search,
        'status': status,
        'status_choices': Cart.STATUS_CHOICES,
    }

    return render(request, 'shop/carts.html', context)