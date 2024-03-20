from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CallHistory

class CallHistoryAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'result', 'call_date')
    list_filter = ('endpoint', 'call_date')
    search_fields = ('endpoint', 'result')
    date_hierarchy = 'call_date'


admin.site.unregister(User)


admin.site.register(User, UserAdmin)


admin.site.register(CallHistory, CallHistoryAdmin)
