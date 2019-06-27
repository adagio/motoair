from django.contrib.admin import AdminSite
from django.contrib import admin

# Register your models here.
from .models import Choice, Question


class MyAdminSite(AdminSite):
    site_header = 'Polls administration'
    site_title = 'Polls site'
    index_title = 'Administration'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin_site = MyAdminSite(name='myadmin')
admin_site.register(Question, QuestionAdmin)
