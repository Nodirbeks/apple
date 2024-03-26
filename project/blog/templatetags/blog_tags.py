from django import template
from blog.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_sorters():
    sorters = {
        '-views': 'Просмотры ⬆️',
        'views': 'Просмотры ⬇️',
        '-title': 'От А до Я',
        'title': 'От Я до А',
        '-created_at': 'Сначала новые',
        'created_at': 'Сначала старые'
    }
    return sorters
