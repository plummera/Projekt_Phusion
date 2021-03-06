"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BootstrapSignUpForm(AuthenticationForm):
    """Signup form which uses boostrap CSS."""
    signUpName = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    signUpEmail = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}))
    signUpEmailAgain = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email (confirm)'}))
    signUpPassword = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    signUpPasswordAgain = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password Again'}))

class DataForm(forms.Form):
    category = forms.CharField(max_length=100)
    metric = forms.CharField(max_length=3)

class User1Form(forms.Form):
    user1 = forms.CharField(max_length=100,
                            widget=forms.TextInput({
                            'class': 'form-control',
                            'placeholder': 'Enter User 1'}))
class User2Form(forms.Form):
    user2 = forms.CharField(max_length=100,
                            widget=forms.TextInput({
                            'class': 'form-control',
                            'placeholder': 'Enter User 2'}))
