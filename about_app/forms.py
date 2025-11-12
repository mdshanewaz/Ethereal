from django import forms
from about_app.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

        widgets = { 
            'name' :  forms.TextInput(attrs={'class': 'form-control mb-2', 'required': 'required'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control mb-2', 'required': 'required'}),
            'phone' : forms.TextInput(attrs={'class':'form-control mb-2', 'type': 'tel'}),
            'grade' : forms.Select(attrs={'class':'form-select form-select-md mb-2', 'aria-label':'.form-select-sm example', 'required': 'required'}),
            'message' : forms.Textarea(attrs={'class': 'form-control mb-2', 'required': 'required', 'rows':'3'}),
         }