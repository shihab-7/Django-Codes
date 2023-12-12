from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = '__all__'
        fields = '__all__'
        # exclude = ['name','address']
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll',
        }
        widgets = {
            'name': forms.TextInput(),
            'roll': forms.NumberInput(),
        }
        help_texts = {
            'name': 'write full Name',
        }

        error_messages = {
            'name': {'required': "name is must "}
        }
# all dile sob field e automatic niye nibe r essa korle shudhu spacefic field add kore rakhate pari models.py er