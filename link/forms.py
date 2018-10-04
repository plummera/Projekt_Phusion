"""
Definition of forms.
"""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': _("This account is inactive."),
    }

class DataForm(forms.Form):
    category = forms.CharField(max_length=100)
    metric = forms.CharField(max_length=3)

class TwitterNameForm(forms.Form):
    twitter_name = forms.CharField(label='Twitter User', max_length=100)

class CryptoForm(forms.Form):
    url = forms.URLField()

class SignUpForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput({
                                    'class': 'form-control radial',
                                    'placeholder': 'Password',
                                    'type': 'password',
                                    'id': 'password1',
                                    'name': 'password1',
                                    'onkeyup': 'passwordChecker()',
                                }),
                                help_text=_("Enter a password"))

    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput({
                                    'class': 'form-control radial',
                                    'placeholder': 'Password Again',
                                    'type': 'password',
                                    'id': 'password2',
                                    'name': 'password2',
                                }),
                                help_text=_("Enter the same password as above, for verification."))

    username = forms.CharField(max_length=30,
                                widget=forms.TextInput({
                                    'class': 'form-control radial',
                                    'placeholder': 'Username',
                                    'type': 'text',
                                    'id': 'username',
                                    'name': 'username',
                                }),
                                required=False, help_text='Required.')
    first_name = forms.CharField(max_length=30,
                                widget=forms.TextInput({
                                    'class': 'form-control radial',
                                    'placeholder': 'First Name',
                                    'type': 'text',
                                    'id': 'yourFirstName',
                                    'name': 'yourFirstName',
                                }),
                                required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30,
                                widget=forms.TextInput({
                                    'class': 'form-control radial',
                                    'placeholder': 'Last Name',
                                    'type': 'text',
                                    'id': 'yourLastName',
                                    'name': 'yourLastName',
                                }),
                                required=False, help_text='Required.')
    email = forms.EmailField(max_length=254,
                                widget=forms.TextInput({
                                    'class': 'form-control radial',
                                    'placeholder': 'Email Address',
                                    'type': 'email',
                                    'id': 'yourEmail',
                                    'name': 'yourEmail',
                                }),
                                help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
