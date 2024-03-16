from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from Employees.models import EmployeeDetail



@receiver(post_save, sender=CustomUser)
def create_employee_signal(sender, instance, created, **kwargs):
    if created:
        EmployeeDetail.objects.create(employee=instance,
                                      first_name=instance.username,
                                      email=instance.email)
        
        
