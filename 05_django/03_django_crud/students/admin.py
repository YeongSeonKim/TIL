from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk','name','age','email','created_at', 'updated_at')

admin.site.register(Student, StudentAdmin)