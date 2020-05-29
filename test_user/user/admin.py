from django.contrib import admin

# Register your models here.

from user.models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
	list_display=('email','is_staff','is_admin','is_student')
	search_fields=('email','is_staff')
	readonly_fields=()
	filter_horizontal=()
	list_filter=()
	fieldsets=()
admin.site.register(Account,AccountAdmin)