from django.contrib import admin

from.models import Book, Author, Address, Country

# Register your models here.
admin.site.site_header = "Book Store Admin Panel"
admin.site.site_title = "Book Store Admin"
admin.site.index_title = "Welcome to the Book Store Management System"


class BookAdmin(admin.ModelAdmin):
  # readonly_fields = ("slug",)
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("author", "rating")
  list_display = ("title", "author", "rating", "is_bestselling")
  search_fields = ["title", "author", "rating"]

class AuthorAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name")

class AddressAdmin(admin.ModelAdmin):
  list_display = ("street","postal_code", "city")

class CountryAdmin(admin.ModelAdmin):
  list_display = ("name", "code")

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)