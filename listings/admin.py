from django.contrib import admin
from .models import Category, Property, PropertyImage
# Register your models here.
class PropertyImageInLine(admin.TabularInline):
    model = PropertyImage
    extra=1
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display=("id","title","city","price","is_published","status","owner")
    search_fields=("title","city","address","slug")
    list_filter=("city","status","property_type","is_published")
    prepopulated_fields={"slug":("title",)}
    inlines=[PropertyImageInLine]
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name","slug")
    prepopulated_fields={"slug":("name",)}
@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display=("id","property","is_cover","order")