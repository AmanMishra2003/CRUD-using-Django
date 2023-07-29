from django import forms
from .models import Employee

class addform(forms.ModelForm):
    class Meta:
        model= Employee
        fields = "__all__"

        widgets = {
            'ename' : forms.TextInput(attrs = {'class':'form-control', 'label': 'Employee', 'autofocus': True}),
            'edept' : forms.TextInput(attrs = {'class':'form-control','label': 'Department'}),
            'esal' : forms.NumberInput(attrs = {'class':'form-control', 'label': 'Salary'})
        }

        labels = {
            'ename' : "Employee Name",
            'edept' : "Department",
            'esal'  : "salary"      
        }

# class updateform(forms.ModelForm):
#     class Meta:
#         model= Employee
#         fields = "__all__"

#         widgets = {
#             'ename' : forms.TextInput(attrs = {'class':'form-control', }),
#             'edept' : forms.TextInput(attrs = {'class':'form-control'}),
#             'esal' : forms.NumberInput(attrs = {'class':'form-control'})
#         }

