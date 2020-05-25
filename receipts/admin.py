from django.contrib import admin
from .models import *

class PaymentsStringInline(admin.TabularInline):
    model = PaymentsString
    extra = 0

class StatusStringInline(admin.TabularInline):
    model = StatusString
    extra = 0

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    inlines = [StatusStringInline]


    class Meta:
        model = Status
admin.site.register(Status, StatusAdmin)

class PaymentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payments._meta.fields]
    inlines = [PaymentsStringInline]


    class Meta:
        model = Payments
admin.site.register(Payments, PaymentsAdmin)
