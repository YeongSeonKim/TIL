from django.contrib import admin
from .models import Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'past_job', 'created_at', 'updated_at')

admin.site.register(Job, JobAdmin)