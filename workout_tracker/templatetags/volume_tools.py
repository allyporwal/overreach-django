from django import template


register = template.Library()


@register.filter(name="get_index")
def get_index(list, i):
    return list[i]
