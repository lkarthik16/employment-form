from django import forms
from .models import EmploymentForm

class EmploymentFormForm(forms.ModelForm):
    class Meta:
        model = EmploymentForm
        fields = '__all__'