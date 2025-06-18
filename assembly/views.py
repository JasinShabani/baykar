from django.shortcuts import render, redirect
from .models import Assembly, AssemblyPart
from production.models import Plane, Part
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def assemble_plane(request):
    if request.user.personnel.team.name != 'ASSEMBLY':
        return HttpResponseForbidden("You do not have permission to access this page.")

    if request.method == 'POST':
        plane_id = request.POST.get('plane_id')
        plane = Plane.objects.get(id=plane_id)

        parts_needed = ['Wing', 'Fuselage', 'Tail', 'Avionics']
        used_parts = []

        missing_parts = []
        for part_type in parts_needed:
            part = Part.objects.filter(part_type=part_type, stock_quantity__gt=0, plane=plane).first()
            
            if not part:
                missing_parts.append(part_type)
            else:
                used_parts.append(part)

        if missing_parts:
            messages.error(request, f'Missing parts: {", ".join(missing_parts)}')
            return render(request, 'assembly/assemble_plane.html', {
                'planes': Plane.objects.all(),
                'selected_plane': plane_id,
                'missing_parts': missing_parts
            })
        
        assembly = Assembly.objects.create(plane=plane, status='COMPLETED')
        for part in used_parts:
            AssemblyPart.objects.create(assembly=assembly, part=part, quantity_used=1)
            part.stock_quantity -= 1
            part.plane = plane
            part.save()

        messages.success(request, f'{plane.name} successfully assembled!')
        return redirect('assembly_success')

    planes = Plane.objects.all()
    return render(request, 'assembly/assemble_plane.html', {'planes': planes})

@login_required
def assembly_success(request):
    return render(request, 'assembly/assembly_success.html')

@login_required
def assembly_report(request):
    assemblies = Assembly.objects.all().prefetch_related('assemblypart_set')
    
    assembly_data = []
    for assembly in assemblies:
        date_assembled_tz = timezone.localtime(assembly.date_assembled, timezone.get_current_timezone())
        
        parts_used = AssemblyPart.objects.filter(assembly=assembly)
        assembly_data.append({
            'plane': assembly.plane.name,
            'date_assembled': date_assembled_tz.strftime('%d/%m/%Y %H:%M'),
            'status': assembly.get_status_display(),
            'parts': parts_used,
        })
    
    return render(request, 'assembly/assembly_report.html', {'assembly_data': assembly_data})
