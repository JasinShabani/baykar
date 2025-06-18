from django.shortcuts import render, redirect, get_object_or_404
from .models import Personnel
from .forms import PersonnelForm, UserRegistrationForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            team = form.cleaned_data['team']
            Personnel.objects.create(user=user, team=team, name=user.get_full_name())
            login(request, user)
            return redirect('personnel_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def personnel_list(request):
    try:
        personnel = Personnel.objects.get(user=request.user)  
        return render(request, 'personnel_list.html', {'personnel': [personnel]})
    except Personnel.DoesNotExist:
        return redirect('login') 

@login_required
def personnel_create(request):
    if Personnel.objects.filter(user=request.user).exists():
        messages.error(request, 'Bu kullanıcıya zaten bir personel atanmış.')
        return redirect('personnel_list')

    if request.method == "POST":
        form = PersonnelForm(request.POST)
        if form.is_valid():
            personnel = form.save(commit=False)
            personnel.user = request.user  
            personnel.save()
            return redirect('personnel_list')  
    else:
        form = PersonnelForm()

    return render(request, 'personnel_create.html', {'form': form})

@login_required
def personnel_update(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)  
    if request.method == "POST":
        form = PersonnelForm(request.POST, instance=personnel)  
        if form.is_valid():
            form.save()  
            return redirect('personnel_list')
    else:
        form = PersonnelForm(instance=personnel) 

    return render(request, 'personnel_update.html', {'form': form})

@login_required
def personnel_delete(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)  
    if request.method == 'POST':
        personnel.delete()
        return redirect('personnel_list')

    return render(request, 'personnel_delete.html', {'personnel': personnel})

@login_required
def personnel_data(request):
    search_value = request.GET.get('search[value]', '') 

    personnels = Personnel.objects.all()

    if search_value:
        personnels = personnels.filter(
            Q(name__icontains=search_value) | Q(team__name__icontains=search_value)  
        )

    data = {
        "draw": int(request.GET.get('draw', 1)),
        "recordsTotal": Personnel.objects.count(),  
        "recordsFiltered": personnels.count(),  
        "data": list(personnels.values('id', 'name', 'team__name')) 
    }
    
    return JsonResponse(data)
