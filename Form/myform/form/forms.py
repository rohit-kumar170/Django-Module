from django import forms
from django.forms import ModelForm
from .models import Author,Book

class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields=["name","title","birth_date"]

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields=["name","authors"]


##send_mail
class ContactForm(forms.Form):
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(required=False)
