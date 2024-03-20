from django.shortcuts import render
from Employees.models import EmployeeDetail, EmployeeAttendance
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse




@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def EmployeeHomePage(request):
    all_employee = EmployeeDetail.objects.all()

    context = {
        'employee': all_employee
    }
    return render(request, 'Employee/emphome.html', context)



class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = EmployeeDetail
    template_name = 'Employee/empdetail.html'

    def test_func(self, request, *args, **kwargs):
        employee = self.get_object()
        
        if self.request.user == employee:
            return True
        return  False
    




#Add two Mixins(LoginRequired and Userpasses Test)
class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = EmployeeDetail
    template_name = 'Employee/empupdate.html'
    fields = "__all__"
    success_url = '/emp/emp-home'

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def test_func(self):
        employee = self.get_object()
        if self.request.user == employee.employee:
            return True
        elif self.request.user.is_staff:
            return True
        return False



class EmployeeDataUpdateView(LoginRequiredMixin, UpdateView):
    model = EmployeeDetail
    template_name = 'Employee/empupdate.html'
    fields = "__all__"
    # success_url = '/emp/emp-detail/'

    def get_success_url(self):
        id = self.kwargs.get('pk')
        return reverse('Employee_Detail', kwargs={'pk': id})



class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = EmployeeDetail
    success_url = '/emp/emp-home'
    template_name = 'Employee/empdelete.html'

    def test_func(self):
        user =  self.request.user
        if user.is_staff:
            return True
        return False




class EmployeeCreateView(CreateView):
    model = EmployeeDetail
    fields = "__all__"

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


@login_required
def IntimeAttendanceReportView(request):
    user = request.user
    attendance_report = None
    employee_detail = None
    attendance_report_success = None

    if request.method == 'POST':    
        try:
            employee_detail = EmployeeDetail.objects.get(employee=user)
        except EmployeeDetail.DoesNotExist:
            employee_detail = "Not Registered as a Employee First Create One"

        try:
            today = timezone.now().date()
            today_attendance = EmployeeAttendance.objects.filter(employee=employee_detail, date__date=today).first()

            if today_attendance:
                attendance_report  = "Already Registered for today try again tomorrow"
            else:
                EmployeeAttendance.objects.create(employee=employee_detail, is_present=True)
                attendance_report_success  = "Successfully Registered your Attendance"
        except EmployeeAttendance.DoesNotExist:
            attendance_report = "No EmployeeAttendance model exists"

    context = {
        'attendance_report': attendance_report,
        'employee_detail': employee_detail,
        'attendance_report_success': attendance_report_success
        }
    
    return render(request, 'Employee/intime.html', context)
    




def OutTimeAttendanceReportView(request, pk):
    # user = request.user
    leavetime_report = None
    leavetime_report_success = None
    
    if request.method == "POST":
        try:
            employee_attendance = EmployeeAttendance.objects.get(pk=pk) 
            if not employee_attendance.out_time:
                employee_attendance.out_time  = datetime.now().time()
                employee_attendance.save()
                leavetime_report_success = "Successfully Registered Leave time"
            else:
                leavetime_report = "Please Try again letter"

        except EmployeeAttendance.DoesNotExist:
            leavetime_report = "No EmployeeAttendance model exists"

    context = {
        'leavetime_report': leavetime_report,
        'leavetime_report_success': leavetime_report_success
    }

    return render(request, 'Employee/outime.html', context)



def EmployeeAttendanceReportView(request, pk):
    try:
        employee = EmployeeDetail.objects.get(id=pk)
    except:
        employee = None
        
    all_employee_attendance = EmployeeAttendance.objects.filter(employee=employee)

    context = {
        'all_employee_attendance': all_employee_attendance
    }
    return render(request, 'Employee/attendance_report.html', context)


