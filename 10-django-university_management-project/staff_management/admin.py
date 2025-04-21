from django.contrib import admin
from .models import Department, Role, Staff

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'role', 'salary', 'hire_date')
    list_filter = ('department', 'role')
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 10
