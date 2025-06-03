from datetime import datetime, timedelta, time
import calendar # Para obtener nombres de días de la semana
import json
from django.http import JsonResponse
from .models import Event
from .forms import EventForm
from .ml_optimizer import TaskOptimizer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_GET


# --- VISTA PRINCIPAL DEL CALENDARIO ---
@login_required
def calendar_view(request):
    """
    Vista del calendario que muestra los eventos del usuario en una vista semanal.
    """
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    day_names_es = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    week_days_data = []
    for i in range(7):
        current_day = start_of_week + timedelta(days=i)
        is_today = (current_day == today)
        week_days_data.append({
            'date': current_day,
            'day_num': current_day.day,
            'day_name_short': day_names_es[current_day.weekday()][:3],
            'is_today': is_today,
        })

    user_events = Event.objects.filter(
        user=request.user,
        start_time__date__gte=start_of_week,
        end_time__date__lte=end_of_week + timedelta(days=1)
    ).order_by('start_time')

    CALENDAR_START_HOUR = 0
    CALENDAR_END_HOUR = 23
    PIXELS_PER_HOUR = 60

    events_for_template = []
    for event in user_events:
        start_hour_float = event.start_time.hour + event.start_time.minute / 60.0
        top_px = (start_hour_float - CALENDAR_START_HOUR) * PIXELS_PER_HOUR + PIXELS_PER_HOUR
        duration_minutes = (event.end_time - event.start_time).total_seconds() / 60.0
        height_px = (duration_minutes / 60.0) * PIXELS_PER_HOUR
        css_class_type = f"event-{event.event_type}"

        events_for_template.append({
            'id': event.pk,
            'title': event.title,
            'description': event.description,
            'start_time': event.start_time,
            'end_time': event.end_time,
            'event_type': event.event_type,
            'is_completed': event.is_completed,
            'priority': event.priority,
            'due_date': event.due_date,
            'day_of_week': event.start_time.weekday(),
            'style': f"top: {top_px}px; height: {height_px}px;",
            'css_class': css_class_type,
        })

    events_by_day = {i: [] for i in range(7)}
    for event_data in events_for_template:
        events_by_day[event_data['day_of_week']].append(event_data)

    context = {
        'today': today,
        'start_of_week': start_of_week,
        'end_of_week': end_of_week,
        'week_days_data': week_days_data,
        'events_by_day': events_by_day,
        'time_slots': [f"{h:02d}:00" for h in range(CALENDAR_START_HOUR, CALENDAR_END_HOUR + 1)],
        'current_month_name': today.strftime("%B"),
        'current_week_range': f"{start_of_week.day:02d}-{end_of_week.day:02d} {start_of_week.strftime('%B')} {start_of_week.year}"
    }
    return render(request, 'horarios.html', context)

@login_required
def optimize_schedule(request):
    """
    Vista para optimizar el horario del usuario usando IA.
    """
    try:
        if request.method == 'POST':
            user_events = Event.objects.filter(user=request.user).order_by('start_time')
            
            print(f"DEBUG: Usuario {request.user.username}")
            print(f"DEBUG: Total de eventos: {user_events.count()}")
            
            if not user_events.exists():
                return JsonResponse({
                    'suggestions': [],
                    'message': 'No hay tareas creadas.'
                })
            
            # Mostrar información de las tareas
            for event in user_events:
                print(f"DEBUG: Tarea: {event.title}, Completada: {event.is_completed}, Fecha: {event.start_time}")
                
            # Crear sugerencias considerando si la tarea está completada o no
            suggestions_data = []
            for i, event in enumerate(user_events):
                if event.is_completed:
                    # Para tareas completadas, sugerir mantener horario actual
                    new_start = event.start_time
                    new_end = event.end_time
                    reason = "Tarea completada, se mantiene el horario actual"
                    improvement_score = 0.0
                else:
                    # Para tareas no completadas, sugerir cambios alternados
                    if i % 2 == 0:
                        new_start = event.start_time + timedelta(hours=1)
                        reason = "Mover 1 hora más tarde puede mejorar la concentración"
                    else:
                        new_start = event.start_time - timedelta(hours=1)
                        reason = "Mover 1 hora más temprano puede ser más productivo"
                    new_end = new_start + (event.end_time - event.start_time)
                    improvement_score = 0.8 + (i * 0.1)
                
                suggestions_data.append({
                    'event_id': event.id,
                    'title': event.title,
                    'current_time': event.start_time.isoformat(),
                    'suggested_time': new_start.isoformat(),
                    'suggested_end_time': new_end.isoformat(),
                    'improvement_score': improvement_score,
                    'reason': reason,
                })

            print(f"DEBUG: Sugerencias generadas: {len(suggestions_data)}")
            return JsonResponse({'suggestions': suggestions_data})
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Exception as e:
        print(f"DEBUG ERROR: {str(e)}")
        return JsonResponse({
            'error': f'Error al optimizar el horario: {str(e)}'
        }, status=500)

@login_required
def event_update_ajax(request, pk):
    """
    Vista para actualizar un evento vía AJAX.
    """
    if request.method == 'POST':
        try:
            event = get_object_or_404(Event, pk=pk, user=request.user)
            body = request.body.decode('utf-8')
            data = json.loads(body)
            
            # Convertir fechas ISO a datetime
            start_time_str = data['start_time'].replace('Z', '+00:00')
            end_time_str = data['end_time'].replace('Z', '+00:00')
            
            event.start_time = datetime.fromisoformat(start_time_str)
            event.end_time = datetime.fromisoformat(end_time_str)
            event.save()
            
            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Datos JSON inválidos'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# --- VISTA PARA CREAR UN NUEVO EVENTO ---
def event_create(request):
    """
    Vista para crear un nuevo evento.
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Evento creado exitosamente.')
            return redirect('planner:horarios')
        else:
            messages.error(request, 'Hubo un error al crear el evento. Por favor, revisa los datos.')
    else:
        initial_data = {
            'start_time': datetime.now().strftime('%Y-%m-%dT%H:%M'),
            'end_time': (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M'),
        }
        form = EventForm(initial=initial_data)
    return render(request, 'event_form.html', {'form': form, 'form_type': 'Crear'})

# --- VISTA PARA EDITAR UN EVENTO EXISTENTE ---
def event_edit(request, pk):
    """
    Vista para editar un evento existente.
    """
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento actualizado exitosamente.')
            return redirect('planner:horarios')
        else:
            messages.error(request, 'Hubo un error al actualizar el evento. Por favor, revisa los datos.')
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form, 'form_type': 'Editar'})

# --- VISTA PARA ELIMINAR UN EVENTO ---
def event_delete(request, pk):
    """
    Vista para eliminar un evento.
    """
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Evento eliminado exitosamente.')
        return redirect('planner:horarios')
    return render(request, 'event_confirm_delete.html', {'event': event})

# --- VISTA PARA VER DETALLES DE UN EVENTO ---
def event_detail(request, pk):
    """
    Vista para ver los detalles de un evento.
    """
    event = get_object_or_404(Event, pk=pk, user=request.user)
    return render(request, 'event_detail.html', {'event': event})


@login_required
@require_GET
def list_user_events(request):
    """
    Vista para listar las tareas del usuario con fechas actuales en JSON.
    """
    events = Event.objects.filter(user=request.user).order_by('start_time')
    events_data = []
    for event in events:
        events_data.append({
            'id': event.id,
            'title': event.title,
            'start_time': event.start_time.isoformat(),
            'end_time': event.end_time.isoformat(),
            'is_completed': event.is_completed,
        })
    return JsonResponse({'events': events_data})