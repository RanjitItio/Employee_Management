from django.urls import path
from .import views




urlpatterns = [
    path('emp-home/',views.EmployeeHomePage, name='Employee_Home_Page'),
    path('emp-detail/<int:pk>/',views.EmployeeDetailView.as_view(), name='Employee_Detail'),
    path('emp-update/<int:pk>/',views.EmployeeUpdateView.as_view(), name='Employee_Update'),
    path('user-emp-update/<int:pk>/',views.EmployeeDataUpdateView.as_view(), name='Own_Data_Update'),
    path('emp-delete/<int:pk>/',views.EmployeeDeleteView.as_view(), name='Employee_Delete'),
    path('intime-attendance/',views.IntimeAttendanceReportView, name='Intime_Attendance'),
    path('outime-attendance/<int:pk>/',views.OutTimeAttendanceReportView, name='Outime_Attendance'),
    path('attendance-report/<int:pk>/',views.EmployeeAttendanceReportView, name='Attendance_Report'),
]


