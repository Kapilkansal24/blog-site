from django.contrib import admin
from .models import UserModel
# Register your models here.
# admin.site.register(UserModel)

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname']
    search_fields = ("firstname",)