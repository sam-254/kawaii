from django import template

from news.models import Category

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/categories_list.html')
def show_categories():
    categories = Category.objects.all()

    return {'categories': categories,'categories_count': len(categories) }