from django.forms import ModelForm,TextInput,Textarea,EmailInput
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("username","email","message")
        widgets = {
            "username":TextInput(attrs={
            'class':'form-control',
            'placeholder':'Ваша имя' 

        }),
        "message":Textarea(attrs={
            'class':'form-control',
            'placeholder':'Your message' 

        }),
        "email":EmailInput(attrs={
            'class': 'input_field contact_form_email'
        })
        }