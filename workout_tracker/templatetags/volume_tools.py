from django import template


register = template.Library()


@register.filter(name='calc_volume')
def calc_volume(reps, weight):
    return reps * weight
