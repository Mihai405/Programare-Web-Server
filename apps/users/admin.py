from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model=User
    ordering=('date_joined',)
    list_display=('email','role',)
    fieldsets = (
        (None, {'fields': ('email', 'role',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User,UserAdminConfig)