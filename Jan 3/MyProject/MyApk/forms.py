from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  # Model should be lowercase
        fields = ['name', 'dateofbirth', 'phonenumber', 'email']  # Corrected 'fields' typo
