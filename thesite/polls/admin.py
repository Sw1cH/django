from django.contrib import admin
from polls.models import Poll, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1

class PollAdmin(admin.ModelAdmin):
	list_filter = ['pub_date']
	search_fields = ['question']
	list_display = ('question', 'pub_date', 'was_published_recently')
	fieldsets = [
	(None, 			{'fields': ['question']}),
	('Details',		{'fields': ['pub_date'], 'classes': ['collapse'] }),
	]
	inlines = [ChoiceInline]
	
class ChoiceAdmin(admin.ModelAdmin):
	list_filter = ['votes']
	list_display = ( 'choice_text','poll', 'votes')
	fields = ['choice_text', 'votes', 'poll']
	
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
