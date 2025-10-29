from django.contrib import admin
from .models import Home

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('ten', 'status', 'ngay_tao', 'luot_xem')
