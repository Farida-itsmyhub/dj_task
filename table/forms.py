from django import forms
from .models import Table


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('name', 'price', 'max_speed', 'year', 'image')