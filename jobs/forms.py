"""Input Validation for title company, description"""
from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location', 'salary']

    def clean_salary(self):
        """Custom validation for salary (must be positive)"""
        salary = self.cleaned_data.get('salary')
        if salary is None:
            raise forms.ValidationError("Salary is required.")
        if salary < 0:
            raise forms.ValidationError("Salary must be a positive number")
        return salary
