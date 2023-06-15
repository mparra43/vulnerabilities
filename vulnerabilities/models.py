from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Filters(models.Model):
    STATE_CHOICES = (
        ('Todas', 'Todas'),
        ('Fixeadas', 'Fixeadas'),
    )

    SEVERITY_CHOICES = (
        ('ALL', 'ALL'),
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    )

    
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='Todas')
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='LOW')
  
    def __str__(self):
        return self


class Vulnerability(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    source_identifier = models.CharField(max_length=50)
    published = models.DateTimeField()
    last_modified = models.DateTimeField()
    vuln_status = models.CharField(max_length=20, default='fixeada')
    def __str__(self):
       return self

class Description(models.Model):
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='descriptions')
    lang = models.CharField(max_length=10)
    value = models.TextField()
    def __str__(self):
        return self.value
    
class Metrics(models.Model):
     VULNERABILITY_LEVEL_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    vulnerability = models.OneToOneField(Vulnerability, on_delete=models.CASCADE, related_name='metrics')
    base_severity = models.CharField(max_length=10, choices=VULNERABILITY_LEVEL_CHOICES)
    def __str__(self):
        return str(self.vulnerability)
    
class Weakness(models.Model):
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='weaknesses')
    def __str__(self):
        return str(self.vulnerability)
    
class Configuration(models.Model):
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='configurations')
    def __str__(self):
        return str(self.vulnerability)
    
class Reference(models.Model):
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='references')
    url = models.URLField()
    source = models.CharField(max_length=50)
    def __str__(self):
         return self.url
