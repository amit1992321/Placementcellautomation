from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, label="User's Name",
                               widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'form-control'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'please enter password',
            'class': 'form-control'
        }
    )
    )
