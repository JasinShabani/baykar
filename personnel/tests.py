from django.test import TestCase
from django.contrib.auth.models import User
from .models import Personnel
from .forms import PersonnelForm 
from production.models import Team

class PersonnelModelTest(TestCase):
    
    def setUp(self):
        self.wing_team = Team.objects.create(name='WING')
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def test_personnel_creation(self):
        personnel = Personnel.objects.create(user=self.user, name='Test Personel', team=self.wing_team)
        
        self.assertEqual(Personnel.objects.count(), 1)
        self.assertEqual(personnel.name, 'Test Personel')
        self.assertEqual(personnel.team.name, 'WING')
    
    def test_personnel_form_valid(self):
        data = {
            'name': 'Test Personel',
            'team': self.wing_team.id,
        }
        form = PersonnelForm(data=data)
        self.assertTrue(form.is_valid())

    def test_personnel_form_invalid(self):
        data = {
            'name': '', 
            'team': self.wing_team.id,
        }
        form = PersonnelForm(data=data)
        self.assertFalse(form.is_valid())
