from django.db import models

class DemoForm(models.Model):
    Name =  models.CharField(max_length=100,blank=False,unique=True)
    
    def __str__(self):
        return f"{self.Name}"