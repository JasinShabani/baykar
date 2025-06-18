from rest_framework import viewsets
from .models import Part, Plane, Team
from .serializers import PartSerializer, PlaneSerializer, TeamSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect,  get_object_or_404
from .forms import PartForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PlaneViewSet(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    http_method_names = ['get', 'post']

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names = ['get']

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('personnel_list')
        else:
            messages.error(request, 'Invalid username or password!')
    
    return render(request, 'registration/login.html')

def custom_logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    if request.user.is_authenticated:
        return redirect('personnel_list')
    return render(request, 'home.html')


@login_required
def part_list(request):
    try:
        team = request.user.personnel.team
        parts = Part.objects.filter(team=team)
        return render(request, 'parts/part_list.html', {'parts': parts})
    except AttributeError:
        messages.error(request, 'Unable to access your personnel information.')
        return redirect('login')

@login_required
def part_create(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            user_team = request.user.personnel.team
            allowed_part_types = {
                'WING': 'WING',
                'FUSELAGE': 'FUSELAGE',
                'TAIL': 'TAIL',
                'AVIONICS': 'AVIONICS',
            }
            team_allowed_part_type = allowed_part_types.get(user_team.name)
            if part.part_type != team_allowed_part_type:
                messages.error(request, f'{user_team.name} can only produce {team_allowed_part_type}.')
                return render(request, 'parts/part_create.html', {'form': form})
            if part.stock_quantity <= 0:
                messages.error(request, 'Stock quantity must be at least 1.')
                return render(request, 'parts/part_create.html', {'form': form})
            if part.plane:
                existing_parts = Part.objects.filter(plane=part.plane, part_type=part.part_type).exists()
                if existing_parts:
                    messages.error(request, 'This part type has already been used in this aircraft.')
                    return render(request, 'parts/part_create.html', {'form': form})
            part.team = user_team
            part.save()
            return redirect('part_list')
        else:
            return render(request, 'parts/part_create.html', {'form': form})
    else:
        form = PartForm()
        return render(request, 'parts/part_create.html', {'form': form})


@login_required
def part_delete(request, pk):
    part = get_object_or_404(Part, pk=pk)
    if part.team == request.user.personnel.team:
        if part.stock_quantity > 1:
            part.stock_quantity -= 1
            part.save()
            messages.success(request, '1 unit of the part has been sent to recycling.')
        else:
            part.delete()
            messages.success(request, 'The part has been completely sent to recycling.')
    return redirect('part_list')

@login_required
def team_parts_list(request):
    user_team = request.user.personnel.team.name
    allowed_teams = ['WING', 'FUSELAGE', 'TAIL', 'AVIONICS']
    if user_team not in allowed_teams:
        return HttpResponseForbidden("You do not have permission to access this page.")
    parts = Part.objects.filter(team=request.user.personnel.team)
    return render(request, 'parts/part_list.html', {'parts': parts})