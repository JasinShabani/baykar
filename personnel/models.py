from django.db import models
from django.contrib.auth.models import User

class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)  
    team = models.ForeignKey('production.Team', on_delete=models.CASCADE) 

    def __str__(self):
        return self.name
