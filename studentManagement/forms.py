from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('nome', 'matricula', 'email', 'serie', 'curso', 'idade', 'conclusao')