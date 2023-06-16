from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Filters(models.Model):
    STATE_CHOICES = (
        ('Todas', 'Todas'),
        ('Fixeada', 'Fixeada'),
    )

    SEVERITY_CHOICES = (
        ('ALL', 'ALL'),
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    )

    
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='Todas')
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='ALL')
  
    def __str__(self):
        return self


class Vulnerability(models.Model):
    id = models.AutoField(primary_key=True)
    source_identifier = models.CharField(max_length=50)
    published = models.DateTimeField()
    last_modified = models.DateTimeField(auto_now=True)
    vuln_status = models.CharField(max_length=20, default='Fixeada')
    def __str__(self):
        return f"Vulnerability: ID={self.id}, Source={self.source_identifier}, Status={self.vuln_status}, Descriptions={self.descriptions}, Metrics={self.metrics}"

class Description(models.Model):
    LANG_CHOICES = [
        ('Inglés ', 'en'),
        ('Español', 'es'),
        
    ]
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='descriptions')
    lang = models.CharField(max_length=10, choices=LANG_CHOICES, default='en')
    value = models.TextField()
    def __str__(self):
        return self.value
    
class Metrics(models.Model):
     VULNERABILITY_LEVEL_CHOICES = [
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    ]
     vulnerability = models.ForeignKey(Vulnerability, related_name='metrics', on_delete=models.CASCADE)
     base_severity = models.CharField(max_length=10, choices=VULNERABILITY_LEVEL_CHOICES, default='LOW')
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
    

