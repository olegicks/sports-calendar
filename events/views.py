from django.views.generic import ListView
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
