from django import template

register = template.Library()


@register.filter(name="add_class")
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})


@register.filter
def clp_format(value):
    return "${:,.0f} CLP".format(value)
