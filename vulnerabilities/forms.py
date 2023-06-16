from django.forms import ModelForm
from .models import Filters, Description, Vulnerability, Metrics


class FiltersForm(ModelForm):
    class Meta:
        model =  Filters
        fields = ['state', 'severity']

class VulnerabilityForm(ModelForm):
    class Meta:
        model =  Vulnerability
        fields = ['source_identifier','published']   

class DescriptionForm(ModelForm):
    class Meta:
        model = Description
        fields = [ 'lang', 'value']

class MetricForm(ModelForm):
    class Meta:
        model = Metrics
        fields = [ 'base_severity' ]
