from django.urls import path

from . import views


app_name = 'shop'


urlpatterns = [
    path('carts/', views.carts_list, name='carts_list'),
]