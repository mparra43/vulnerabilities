from django.forms import ModelForm
from .models import Filters
from .models import Vulnerability

class FiltersForm(ModelForm):
    class Meta:
        model =  Filters
        fields = ['state', 'severity']

class VulnerabilityForm(ModelForm):
    class Meta:
        model =  Vulnerability
        fields = ['id','source_identifier','published']   

class DescriptionForm(ModelForm):
    class Meta:
        model = Description
        fields = ['vulnerability', 'lang', 'value']
