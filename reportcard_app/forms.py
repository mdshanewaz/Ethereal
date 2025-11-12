from django import forms
from reportcard_app.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        models = StudentModel
        fields = ['student_name', 'student_class', 'student_id']

class EnglishForm(forms.ModelForm):
    class Meta:
        model = EnglishliteracyModel
        exclude = ['student_name', 'total_mark', 'grade']

class NumeracyForm(forms.ModelForm):
    class Meta:
        models = NumeracyModel
        exclude = ['student_name', 'total_mark', 'grade']

class AwarenessForm(forms.ModelForm):
    class Meta:
        models = AwarenessModel
        exclude = ['student_name', 'total_mark', 'grade']

class BengaliForm(forms.ModelForm):
    class Meta:
        models = BengaliliteracyModel
        exclude = ['student_name', 'total_mark', 'grade']