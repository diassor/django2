from django.contrib import admin
from .models import Proyect

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register(Proyect, ProjectAdmin)
