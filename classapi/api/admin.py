from django.contrib import admin
from api.models import classes,student
# Register your models here.
class classadmin(admin.ModelAdmin):
    list_display=('name','teacher','type')


admin.site.register(classes,classadmin)
admin.site.register(student)

