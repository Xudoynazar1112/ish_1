from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'first_name', "last_name", 'email')
    list_display = ("username", 'first_name', 'last_name', "email")


admin.site.register(User, UserAdmin)
