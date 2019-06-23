from django import forms
from . import models


class TPO_reg_form(forms.ModelForm):
    class Meta:
        model = models.TpoDetails
        fields = ['user',
                  'tpo_mobile']


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=120, label="Username", widget=forms.TextInput(
        attrs={
            'placeholder': 'Username'
        }))
    first_name = forms.CharField(max_length=200, label="First's Name",
                                 widget=forms.TextInput(
                                     attrs={
                                         'placeholder': 'First Name'
                                     }))
    last_name = forms.CharField(max_length=200)
    mobile = forms.CharField(max_length=10, min_length=10)
    email = forms.EmailField(max_length=200, required=False)
    password = forms.CharField(max_length=200)
    repassword = forms.CharField(max_length=200)

    def clean(self):
        # import pdb; pdb.set_trace()
        if self.cleaned_data['password'] != self.cleaned_data['repassword']:
            raise forms.ValidationError(('Password mismatch'), code='invalid')
