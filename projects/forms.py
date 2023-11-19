from django import forms
from .models import Project , Task
class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'category':forms.Select()
        }

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'status':forms.Select()
        }
class TaskCreateForm(forms.ModelForm):
    class Meta:
        model= Task
        fields=['description','is_completed','project']
        widgets = {
            'description':forms.Textarea(),
            'is_completed':forms.CheckboxInput()
        }