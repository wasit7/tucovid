from django.contrib import admin
from account.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Profile._meta.get_fields() ]
    search_fields = [
        'full_name',
        'phone_no',
    ]
