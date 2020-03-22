from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from solarpv.models import User

class user_admin(UserAdmin):
    list_display = ('username', 'email', 'prefix', 'firstname', 'middlename', 'lastname', 'job_title', 'officephone', 'cellphone', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('username', 'email')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, user_admin)
