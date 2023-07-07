from django.forms import ModelForm, TextInput,Textarea,EmailInput
from .models import Comments

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ("name","email","message")
        widgets = {
            "name":TextInput(attrs={
            'class':'input_field contact_form_name',
            'placeholder':'Ваша имя' 

        }),
        "message":Textarea(attrs={
            'class':'text_field contact_form_message',
            'placeholder':'Your message' 

        }),
        "email":EmailInput(attrs={
            'class': 'input_field contact_form_email'
        })
        }