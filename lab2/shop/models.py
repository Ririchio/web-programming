from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Cart(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активна'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='carts'
    )

    products = models.ManyToManyField(
        Product,
        related_name='carts'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Корзина #{self.id} — {self.customer}'

    def products_count(self):
        return self.products.count()