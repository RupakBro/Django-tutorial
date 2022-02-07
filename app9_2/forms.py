from django import forms

class PersonForm2(forms.Form):
    full_name = forms.CharField()
    email_address = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)

