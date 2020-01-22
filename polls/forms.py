from django import forms

class QuestionForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    description = forms.CharField(label='Description', max_length=500)
