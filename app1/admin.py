from django.contrib import admin
from app1.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['st_name','st_age','st_email','st_number']
admin.site.register(Student,StudentAdmin)
