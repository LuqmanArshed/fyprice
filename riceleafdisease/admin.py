from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Training,Check

@admin.register(Training)
class PersonAdmin(ImportExportModelAdmin):
    pass



admin.site.register(Check)
