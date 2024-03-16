from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from Employees.models import EmployeeDetail, EmployeeAttendance
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone
from users.models import CustomUser
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from users.utils import Util





def HomePage(request):
    user = request.user
    employee_id = None
    employee_detail = None
    employee_attendance_id = None

    if user.is_authenticated:
        try:
            employee_detail = EmployeeDetail.objects.get(employee=user)
            employee_id = employee_detail.id
        except EmployeeDetail.DoesNotExist:
            employee_id = None
            employee_detail = None
        
        try:
            today = timezone.now().date()
            employee_attendance = EmployeeAttendance.objects.get(employee=employee_detail, date__date=today)
            employee_attendance_id = employee_attendance.pk
        except EmployeeAttendance.DoesNotExist:
            employee_attendance_id = None

    else:
        employee_id = None
        employee_detail = None
    
    context = {
        'employee_id': employee_id,
        'employee_detail': employee_detail,
        'employee_attendance_id': employee_attendance_id
    }

    return render(request, 'Users/home.html', context)




def RegisterView(request):
    if request.method == 'POST':

        username            = request.POST.get('username')
        email               = request.POST.get('email')
        password            = request.POST.get('password')
        confirm_password    = request.POST.get('confirm_password')
        
        if not (username and email and password and confirm_password):
            messages.error(request, 'Please fill in all the fields.')
            return redirect('Register')

        if password != confirm_password:
            messages.error(request, 'Passwords did not match.')
            return redirect('Register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('Register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('Register')

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, f"Dear {username}, your account has been created successfully. Please login.")
        return redirect('Login')


    return render(request, 'Users/register.html')





def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_message = "Invalid email or password."
        else:
            error_message = "Email and Password is Required"
    else:
        error_message = None
            
    return render(request, 'Users/login.html', {'error_message': error_message})



def LogoutView(request):
    user = request.user
    if user is not None:
        logout(request)
    return render(request, 'Users/logout.html')





@login_required
def ChangePasswordView(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST )
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('Login')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form
    }

    return render(request, 'Users/change_password.html', context)



def PasswordResetView(request):

    if request.method == "POST":
        email = request.POST.get('email')
        
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            token = PasswordResetTokenGenerator().make_token(user)

            link = 'http://127.0.0.1:8000/password-reset-done/'+uid+'/'+token

            body = 'Click Following Link to Reset Your Password '+link
            data = {
                'subject':'Reset Your Password',
                'body':body,
                'to_email':user.email
                }
            Util.send_email(data)
            messages.success(request, "Email sent successfully")
            return redirect('Password_Reset_Confirm')
        else:
            messages.error(request, "Email is not registered")

    return render(request, 'Users/password_reset.html')



def PasswordResetConfirmView(request):
    return render(request, 'Users/password_reset_confirm.html')



def PasswordResetDoneView(request, uid, token):

    if request.method == "POST":
        password = request.POST.get("password")
        password2 = request.POST.get("confirm_password")
        token = token
        uid = uid

        if password != password2:
            messages.error(request, "Password Mismatch")

        id = smart_str(urlsafe_base64_decode(uid))
        user = CustomUser.objects.get(id=id)

        if not PasswordResetTokenGenerator().check_token(user, token):
            messages.error(request, "Token is not valid or Expired")

        user.set_password(password)
        user.save()
        messages.success(request, "Password Reset successfully")

    return render(request, 'Users/password_reset_done.html')


# class UserPasswordResetSerializer(serializers.Serializer):
#   password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
#   password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
#   class Meta:
#     fields = ['password', 'password2']

#   def validate(self, attrs):
#     try:
#       password = attrs.get('password')
#       password2 = attrs.get('password2')
#       uid = self.context.get('uid')
#       token = self.context.get('token')
#       if password != password2:
#         raise serializers.ValidationError("Password and Confirm Password doesn't match")
#       id = smart_str(urlsafe_base64_decode(uid))
#       user = User.objects.get(id=id)
#       if not PasswordResetTokenGenerator().check_token(user, token):
#         raise serializers.ValidationError('Token is not Valid or Expired')
#       user.set_password(password)
#       user.save()
#       return attrs
#     except DjangoUnicodeDecodeError as identifier:
#       PasswordResetTokenGenerator().check_token(user, token)
#       raise serializers.ValidationError('Token is not Valid or Expired')
  