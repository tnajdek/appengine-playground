# django.contrib.markup can't do this and is deprecated anyways
from django import template
from django.template.defaultfilters import stringfilter
from markdown import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='markdown2html')
@stringfilter
def markdown2html(value):
	"""

	"""
	return mark_safe(markdown(value, safe_mode="escape"))
