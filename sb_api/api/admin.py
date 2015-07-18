from django.contrib import admin
from .models import BackScratcher

class BackScratcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(BackScratcher, BackScratcherAdmin)


