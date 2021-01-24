import markdown as md
from django import template

register = template.Library()


@register.filter
def markdown(content):
    return md.markdown(content, extensions=['tables'])
