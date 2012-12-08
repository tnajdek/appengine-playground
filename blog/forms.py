from django.forms import ModelForm
from models import Post
from django import forms

# from django.forms import widgets

# from django.conf import settings
# from django.template.loader import render_to_string
# from django.utils.safestring import mark_safe


# class MarkdownWidget(widgets.TextInput):
# 	class Media:
# 		js = ('Markdown.Converter.js', 'Markdown.Sanitizer.js', 'Markdown.Editor.js')

# 	def render(self, name, value, attrs=None):
# 		return mark_safe(render_to_string('_widgets/markdown.html', {
# 			"name": name,
# 			"value": value,
# 			"STATIC_URL": settings.STATIC_URL  # middleware won't work here
# 		}))


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'permalink', 'visibility', 'text')
		widgets = {
			'permalink': forms.TextInput(attrs={
				'data-provide': 'permalink',
				'data-based-on': 'title'
			}),
			'text': forms.Textarea(attrs={
				'data-provide': 'markdown',
			})
		}
