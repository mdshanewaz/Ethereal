from django import forms
from django.forms import inlineformset_factory
from academic_app.models import PersonalModel, EducationModel, TrainingModel, ExperienceModel, SkillModel, ReferenceModel

class PersonalForm(forms.ModelForm):
    class Meta:
        model = PersonalModel
        fields = '__all__'

        widgets = { 
            'name' :  forms.TextInput(attrs={'class': 'form-control mb-2', 'required': 'required'}),
            'father_name' : forms.TextInput(attrs={'class': 'form-control mb-2', 'required': 'required'}),
            'mother_name' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'permanent_address' : forms.Textarea(attrs={'class':'form-control mb-2', 'rows':'5', 'id':'comment', 'required': 'required'}),
            'present_address' : forms.Textarea(attrs={'class':'form-control mb-2', 'rows':'5', 'id':'comment', 'required': 'required'}),
            'contact_num_1' : forms.TextInput(attrs={'class':'form-control mb-2', 'type': 'tel', 'required': 'required'}),
            'contact_num_2' : forms.TextInput(attrs={'class':'form-control mb-2', 'type': 'tel'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control mb-2', 'required': 'required'}),
            'married' : forms.Select(attrs={'class':'form-select form-select-md mb-2', 'aria-label':'.form-select-sm example', 'required': 'required'}),
            'spouse_name' : forms.TextInput(attrs={'class': 'form-control mb-2',}),
            'religon' : forms.Select(attrs={'class':'form-select form-select-md mb-2', 'aria-label':'.form-select-sm example', 'required': 'required'}),
            'gender' : forms.Select(attrs={'class':'form-select form-select-md mb-2', 'aria-label':'.form-select-sm example', 'required': 'required'}),
            'photo' :  forms.FileInput(attrs={'class': 'form-control-file mb-3', 'required': 'required'}),
            'signature' : forms.FileInput(attrs={'class': 'form-control-file mb-3', 'required': 'required'}),    
         }

class CustomEducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = '__all__'
        widgets = {
            'masters': forms.NumberInput(attrs={'class': 'form-control mb-3', 'min':1980, 'max':2025, 'required': 'required'}),
            'result_1' : forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'group_subject_1' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'institute_1' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'board_faculty_1' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),

            'bachelor': forms.NumberInput(attrs={'class': 'form-control mb-3', 'min':1980, 'max':2025, 'required': 'required'}),
            'result_2' : forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'group_subject_2' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'institute_2' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'board_faculty_2' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),

            'hsc': forms.NumberInput(attrs={'class': 'form-control mb-3', 'min':1980, 'max':2025, 'required': 'required'}),
            'result_3' : forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'group_subject_3' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'institute_3' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'board_faculty_3' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),

            'ssc': forms.NumberInput(attrs={'class': 'form-control mb-3', 'min':1980, 'max':2025, 'required': 'required'}),
            'result_4' : forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'group_subject_4' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'institute_4' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'board_faculty_4' : forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
        }

EducationFormSet = inlineformset_factory(
    PersonalModel, EducationModel,
    form=CustomEducationForm,
    fields='__all__',
    extra=1, 
    can_delete=True
)

class CustomTrainingForm(forms.ModelForm):
    class Meta:
        model = TrainingModel
        fields = '__all__'
        widgets = {
            'title_1': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'year_1': forms.NumberInput(attrs={'class': 'form-control mb-3', 'min':1980, 'max':2025,}),
            'result_1' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'duration_1' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'institute_1' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'title_2': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'year_2': forms.NumberInput(attrs={'class': 'form-control mb-3', 'min':1980, 'max':2025,}),
            'result_2' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'duration_2' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'institute_2' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }

TrainingFormSet = inlineformset_factory(
    PersonalModel, TrainingModel,
    form=CustomTrainingForm,
    fields='__all__',
    extra=1, 
    can_delete=True
)

class CustomExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = '__all__'
        widgets = {
            'position_1': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'duration_1' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'department_1' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'institute_1' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'responsibility_1' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'position_2': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'duration_2' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'department_2' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'institute_2' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'responsibility_2' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }

ExperienceFormSet = inlineformset_factory(
    PersonalModel, ExperienceModel,
    form=CustomExperienceForm,
    fields='__all__',
    extra=1, 
    can_delete=True
)

class CustomSkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'class':'form-control mb-3', 'rows':'5', 'id':'comment', 'required': 'required'}),
        }

SkillFormSet = inlineformset_factory(
    PersonalModel, SkillModel,
    form=CustomSkillForm,
    fields='__all__',
    extra=1, 
    can_delete=True
)

class CustomReferenceForm(forms.ModelForm):
    class Meta:
        model = ReferenceModel
        fields = '__all__'
        widgets = {
            'name_1': forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'contact_info_1': forms.Textarea(attrs={'class':'form-control mb-3', 'rows':'5', 'id':'comment', 'required': 'required'}),
            'name_2': forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
            'contact_info_2': forms.Textarea(attrs={'class':'form-control mb-3', 'rows':'5', 'id':'comment', 'required': 'required'}),
        }

ReferenceFormSet = inlineformset_factory(
    PersonalModel, ReferenceModel,
    form=CustomReferenceForm,
    fields='__all__',
    extra=1, 
    can_delete=True
)