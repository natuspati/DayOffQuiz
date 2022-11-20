from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
    return format_html("</div>")


@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)


@register.simple_tag
def endcol():
    return format_html("</div>")


@register.simple_tag(takes_context=True)
def convert_time(context, unit):
    t_in_s = context['expiration_time']
    if unit == "m":
        return t_in_s // 60
    elif unit == "h":
        return t_in_s // 3600
    elif unit == "d":
        return t_in_s / 3600 // 24
    elif unit == "w":
        return t_in_s / 3600 / 24 // 7
    return t_in_s
