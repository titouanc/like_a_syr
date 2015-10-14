from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from .models import Home


# Register your models here.
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'status', 'dispo_from', 'dispo_to',
        'places', 'languages', 'phone', 'services', 'user_prefs', 'remarks')
    list_filter = (
        ('dispo_from', DateRangeFilter),
        ('dispo_to', DateRangeFilter))
