from django import forms
from API.models import prompt_data

class PromptForm(forms.ModelForm):
    class Meta:
        model = prompt_data
        fields = "__all__"