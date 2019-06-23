from django import forms
from . import models

class StuJobPostApply(forms.ModelForm):

    class Meta:
        model = models.JobApplication
        fields = ['skills', 'achievement', 'resume']