from django.contrib import admin
from .models import Employee, LeaveType, Position, LeaveDate,Type
# Register your models here.

admin.site.register(Employee)
admin.site.register(LeaveType)
admin.site.register(Position)
admin.site.register(LeaveDate)
admin.site.register(Type)
