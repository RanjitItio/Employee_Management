from django.contrib import admin
from Employees.models import EmployeeDetail, EmployeeAttendance, Department



class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department')
    # autocomplete_fields = ['department']
    # search_fields = ['department']

class EmployeeAttendanceModelAdmin(admin.ModelAdmin):
    list_display  = ('employee', 'date', 'in_time', 'out_time','is_present')



admin.site.register(EmployeeDetail, EmployeeModelAdmin)
admin.site.register(EmployeeAttendance, EmployeeAttendanceModelAdmin)
admin.site.register(Department)

