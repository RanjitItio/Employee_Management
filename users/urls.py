from django.urls import path
from .import views



urlpatterns = [
    path('', views.HomePage, name='Home_Page'),
    path('register/', views.RegisterView, name='Register'),
    path('login/', views.LoginView, name='Login'),
    path('logout/', views.LogoutView, name='Logout'),
    path('change-password/', views.ChangePasswordView, name='Change_Password'),
    path('password-reset/', views.PasswordResetView, name='Password_Reset'),
    path('password-reset-confirm/', views.PasswordResetConfirmView, name='Password_Reset_Confirm'),
    path('password-reset-done/<uid>/<token>/', views.PasswordResetDoneView, name='Password_Reset_Done'),
]


