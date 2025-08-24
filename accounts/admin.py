from django.contrib import admin
from .models import UserData

admin.site.register(UserData)
# @admin.register(UserData)
# class UserAdmin(admin.ModelAdmin):
#     list_display= ("id","username","email","phone","is_staff")
#     search_fields= ("username","email","name")