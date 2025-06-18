from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=100)
    part_type = models.CharField(max_length=50, choices=[('WING', 'Wing'), ('FUSELAGE', 'Fuselage'), ('TAIL', 'Tail'), ('AVIONICS', 'Avionics')])
    stock_quantity = models.IntegerField(default=0)
    team = models.ForeignKey('production.Team', on_delete=models.CASCADE)
    plane = models.ForeignKey('production.Plane', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Plane(models.Model):
    PLANE_MODELS = (
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'AKINCI'),
        ('KIZILELMA', 'KIZILELMA'),
    )
    
    name = models.CharField(max_length=50, choices=PLANE_MODELS)
    parts = models.ManyToManyField('Part', through='PlanePart', related_name='planes')

    def __str__(self):
        return self.name

class Team(models.Model):
    TEAM_TYPES = (
        ('WING', 'Wing Team'),
        ('FUSELAGE', 'Fuselage Team'),
        ('TAIL', 'Tail Team'),
        ('AVIONICS', 'Avionics Team'),
        ('ASSEMBLY', 'Assembly Team'),
    )
    
    name = models.CharField(max_length=100, choices=TEAM_TYPES)

    def __str__(self):
        return self.name

class PlanePart(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity_used = models.IntegerField(default=1)

    class Meta:
        unique_together = ('plane', 'part')
