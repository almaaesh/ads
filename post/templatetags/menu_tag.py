from django import template
from post.models import Category

register = template.Library()

@register.inclusion_tag('_category_menu.html')
def get_category_menu():
    category_menu = Category.get_categories()
    return {
        'menu_list': category_menu,
    }