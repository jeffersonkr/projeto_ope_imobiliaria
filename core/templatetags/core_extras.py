from django import template


def div(value):
    return "{0:.2f}".format(value/12)


register = template.Library()
register.filter('div', div)
