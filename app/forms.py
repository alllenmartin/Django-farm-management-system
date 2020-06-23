from django import forms
from . models import Farm

class FarmForm(forms.ModelForm):

    class Meta:
        model = Farm
        fields = ['farm_name','farm_number', 'scheme']