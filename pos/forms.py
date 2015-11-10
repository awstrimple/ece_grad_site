from django import forms
from pos.models import Student

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=20)
    your_other_name = forms.CharField(max_length=20)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

