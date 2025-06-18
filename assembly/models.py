from django.db import models
from production.models import Plane, Part

class Assembly(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    date_assembled = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        choices=[('COMPLETED', 'Completed'), ('INCOMPLETE', 'Incomplete')],
        default='INCOMPLETE'
    )  

    def __str__(self):
        return f"{self.plane.name} assembly - {self.get_status_display()}"


class AssemblyPart(models.Model):
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity_used = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.part.name} - {self.quantity_used} units"
