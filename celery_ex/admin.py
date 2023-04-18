from django.contrib import admin

from celery_ex.models import Celery_ex_Author, Celery_ex_Quotes


class QuotesInline(admin.StackedInline):
    model = Celery_ex_Quotes
    extra = 1


@admin.register(Celery_ex_Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('text', 'authors')
    list_filter = ['text', 'authors']
    search_fields = ['text', 'authors']


@admin.register(Celery_ex_Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',  'description')
    list_filter = ['name']
    search_fields = ['name']
    inlines = [QuotesInline]