from django.contrib import admin
from app1.models import Student
from app1.models import User

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['st_name','st_age','st_email','st_number']
admin.site.register(Student,StudentAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['us_name','us_age','us_email','us_phone']

admin.site.register(User,UserAdmin)
