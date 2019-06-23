from django import forms
from . import models


class Stu_Form_per(forms.ModelForm):
    class Meta:
        model = models.StudentPersonalDetail
        fields = ['user',
                  'gender',
                  'uid',
                  'image',
                  'mobile',
                  'alternate_mobile',
                  'father_name',
                  'mother_name',
                  'temperory_address',
                  'permanent_address',
                  ]


class Stu_Form_edu(forms.ModelForm):
    class Meta:
        model = models.StudentEducationalQualifications
        fields = ['high_school_name',
                  'high_school_board',
                  'inter_school_name',
                  'inter_school_board',
                  'bachlors_collage_name',
                  'pg_collage_name',
                  'highschool_grade',
                  'highschool_obtain_marks',
                  'highschool_max_marks',
                  'inter_grade',
                  'inter_obtain_marks',
                  'inter_max_marks',
                  'bachalors_pursuing',
                  'bachalors_obtain_marks',
                  'bachalors_max_marks',
                  'pg_pursuing',
                  'pg_obtain_marks',
                  'pg_total_marks',
                  ]


class Stu_Form_pro(forms.ModelForm):
    class Meta:
        model = models.StudentJobApplicationDetail
        fields = ['skills', 'achievement']


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
