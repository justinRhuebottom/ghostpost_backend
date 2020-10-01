from django.contrib import admin

from ghostpostApp.models import ghostpost

admin.register(ghostpost)(admin.ModelAdmin)