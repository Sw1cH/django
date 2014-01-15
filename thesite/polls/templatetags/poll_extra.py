from django import template

register = template.Library()

# /polls/templates/poll_render.html
# /polls/templatetags/poll_extra.py
@register.inclusion_tag('poll_render.html')
def poll_messages(messages):
	return {'messages': messages}

@register.inclusion_tag('language_selection.html')	
def	lang_select():
	return {}



