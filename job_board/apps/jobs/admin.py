from django.contrib import admin
from .models import Category, Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
  list_display = ('title', 'salary', 'description')
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("salary", "title")

admin.site.register(Category)
admin.site.register(Job, JobAdmin)