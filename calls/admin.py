from django.contrib import admin
from .models import CallRecord, Bill



class CallRecordAdmin(admin.ModelAdmin):
    pass


class BillAdmin(admin.ModelAdmin):
    pass


admin.site.register(CallRecord, CallRecordAdmin)
admin.site.register(Bill, BillAdmin)

