from django.contrib import admin

from .models import Book


# admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    list_filter = ['price']

admin.site.register(Book, BookAdmin)

# 裝飾器


#class BookAdmin(admin.ModelAdmin):
#    list_display = ['name', 'price']
#    search_fields = ['name']
#    list_filter = ['price']



