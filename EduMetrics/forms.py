from django import forms
from .models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ["name", "county", "num_teachers", "num_learners", "has_electricity", "has_infrastructure"]