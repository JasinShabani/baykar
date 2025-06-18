# production/tests.py
from django.test import TestCase
from .models import Team, Plane

class TeamModelTest(TestCase):
    
    def setUp(self):
        Team.objects.create(name='WING')
        Team.objects.create(name='FUSELAGE')

    def test_team_name(self):
        wing_team = Team.objects.filter(name='WING').first()
        fuselage_team = Team.objects.filter(name='FUSELAGE').first()
        self.assertEqual(wing_team.name, 'WING')
        self.assertEqual(fuselage_team.name, 'FUSELAGE')

class PlaneModelTest(TestCase):
    
    def setUp(self):
        Plane.objects.create(name='TB2')
        Plane.objects.create(name='AKINCI')

    def test_plane_name(self):
        tb2_plane = Plane.objects.filter(name='TB2').first()
        akinci_plane = Plane.objects.filter(name='AKINCI').first()
        self.assertEqual(tb2_plane.name, 'TB2')
        self.assertEqual(akinci_plane.name, 'AKINCI')
