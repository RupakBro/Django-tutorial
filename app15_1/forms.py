from django import forms


class EmailForm(forms.Form):
    to = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))