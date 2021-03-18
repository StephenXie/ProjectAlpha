from django import forms

class GPACalForm(forms.Form):
    class_name = forms.CharField(label = "class_name")
    grade = forms.CharField(label = "class_name")
    class_type = forms.CharField(label = "class_name")