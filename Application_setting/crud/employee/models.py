from pickle import FALSE
from django.db import models  
from django.core.validators import MinValueValidator,MaxValueValidator

class Employee(models.Model):  
    id = models.AutoField(primary_key=True) 
    module = models.CharField(max_length=50,null=FALSE) 
    setting_name = models.CharField(max_length=50,unique=True)   
    setting_id = models.TextField(max_length=250) 
    is_enabled = models.SmallIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(1)])

   
   
    def __str__(self):
        return self.module
