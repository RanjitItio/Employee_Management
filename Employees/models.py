from django.db import models
from users.models import CustomUser
from django.utils import timezone



GENDER = (
    ('Male', "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)



class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Department Name")

    def __str__(self):
        return self.name
    


class EmployeeDetail(models.Model):
    employee      = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                                      related_name='employee')
    emp_id        = models.CharField(max_length=30, null=True, blank=True,
                                      verbose_name="Employee ID")
    first_name    = models.CharField(max_length=100, verbose_name="First Name", null=True, blank=True)
    last_name     = models.CharField(max_length=100, verbose_name="Last Name", null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    department    = models.ForeignKey(Department, on_delete=models.CASCADE,
                                       verbose_name="Department", null=True, blank=True)
    profile_pic   = models.ImageField(default='Employee/Profilepic/profile.png',
                                       upload_to='Employee/Profilepic',
                                         verbose_name="Profile Pic")
    mobile_number = models.CharField(max_length=12, verbose_name="Mobile Number",
                                      null=True, blank=True, unique=True)
    email         = models.CharField(max_length=225, verbose_name="Email ID",
                                     null=True, blank=True, unique=True)
    gender        = models.CharField(choices=GENDER, max_length=50, verbose_name="Gender", null=True, blank=True)
    designation   = models.CharField(max_length=100, null=True, blank=True,
                                      verbose_name="Designation")
    salary        = models.CharField(max_length=20, null=True, blank=True, 
                                     verbose_name="Salary Package")
    address       = models.CharField(max_length=300, null=True, blank=True, 
                                     verbose_name="Address")
    is_active     = models.BooleanField(default=True, verbose_name="Status")
    joining_date  = models.DateField(auto_now_add=True, verbose_name="Joining Date")
    leaving_date  = models.DateField(verbose_name="Leaving Date", null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



class EmployeeAttendance(models.Model):
    employee   = models.ForeignKey(EmployeeDetail, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False, verbose_name="Present Status")
    # date       = models.DateTimeField(auto_now_add=True,verbose_name="Date")
    date       = models.DateTimeField(default=timezone.now,verbose_name="Date")
    in_time    = models.TimeField(auto_now_add=True, verbose_name="In Time")
    out_time   = models.TimeField(verbose_name="Out Time", null=True, blank=True)



    def __str__(self):
        return f"{self.employee.first_name}  {self.employee.last_name} is {self.is_present}"
    


    