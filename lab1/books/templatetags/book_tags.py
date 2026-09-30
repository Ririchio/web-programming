from datetime import datetime

from django import template


register = template.Library()


@register.filter
def rubles(value):
    return f'{value} ₽'


@register.filter
def book_size(pages):
    if pages < 300:
        return 'небольшая'
    elif pages < 500:
        return 'средняя'
    return 'большая'


@register.filter
def availability_text(value):
    if value:
        return 'В наличии'
    return 'Нет в наличии'


@register.simple_tag
def books_count(books):
    return len(books)


@register.simple_tag
def available_count(books):
    return sum(book.is_available for book in books)


@register.simple_tag
def current_year():
    return datetime.now().year