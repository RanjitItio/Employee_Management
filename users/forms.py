from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser
from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2'] 


class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=200)
    password = forms.CharField(max_length=30, required=True, label="Password", strip=False, widget=forms.PasswordInput)

    # class Meta:
    #     model = CustomUser
    #     fields = ['email', 'password']


class PasswordChangeForm(forms.Form):
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    old_password = forms.CharField(label=_("Old password"), strip=False,
        widget=forms.PasswordInput(),)
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)


    def clean_old_password(self):
        
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password
    
    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


