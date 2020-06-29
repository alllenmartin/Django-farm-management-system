from django import forms
from . models import Farm

class FarmForm(forms.ModelForm):
    farm_name = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder': 'eg. Wabriwe'}))
    farm_number = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder': 'eg. 087'}))
    mobile_number = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder': 'eg. 0712345678'}))
    other_number = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder': 'eg. 0712345678'}))
    address = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder': 'eg. Box 0000 Ahero'}))


    class Meta:
        model = Farm
        fields = ['farm_name','farm_number', 'other_number', 'address', 
        'mobile_number', 'cultivation_plan', 'capital','scheme']


    def __init__(self, *args, **kwargs):
        super(FarmForm,self).__init__(*args,**kwargs)
        self.fields['scheme'].empty_label= "Select"
        self.fields['cultivation_plan'].required= False
        self.fields['other_number'].required= False

