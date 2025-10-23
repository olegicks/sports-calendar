from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import EventForm
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all().select_related(
            'stage__competition__sport',
            'home_team',
            'away_team',
            'venue',
            'winner'
        ).order_by('start_datetime')


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_create.html'
    success_url = reverse_lazy('events:event-list')