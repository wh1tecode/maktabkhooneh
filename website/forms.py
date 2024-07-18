from django import forms
from website.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ["created_date", "updated_date"]