from django.contrib import admin
from django.forms import TextInput, Textarea

# Register your models here.
from .models import Adventure

class AdventureAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Adventure',               {'fields': ['title', 'a_slug', 'header_image']}),
        ('Info',                    {'fields': ['short_description']}),
        ('Dates',  {'fields': ['start_date', 'end_date']}),
        ('Price',  {'fields': ['price', 'stripe_price', 'single_payment']}),
    ]
    list_display = ('title', 'price', 'start_date', 'end_date')
admin.site.register(Adventure, AdventureAdmin)
