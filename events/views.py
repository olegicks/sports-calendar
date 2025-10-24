from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .forms import EventForm, EventUpdateForm, TeamForm, VenueForm, StageForm, CompetitionForm, SportForm
from .models import Event, Team, Venue, Stage, Competition, Sport


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


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        return super().get_queryset().select_related(
            'stage__competition__sport',
            'home_team',
            'away_team',
            'venue',
            'winner'
        )


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventUpdateForm
    template_name = 'events/event_update.html'

    def get_success_url(self):
        return reverse_lazy('events:event-detail', kwargs={'pk': self.object.pk})


class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'events/team_create.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('events:event-list')


class VenueCreateView(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'events/venue_create.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('events:event-list')


class VenueCreateView(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'events/venue_create.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('events:event-list')


class SportCreateView(CreateView):
    model = Sport
    form_class = SportForm
    template_name = 'events/sport_create.html'
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('events:event-list')


class CompetitionCreateView(CreateView):
    model = Competition
    form_class = CompetitionForm
    template_name = 'events/competition_create.html'
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('events:event-list')


class StageCreateView(CreateView):
    model = Stage
    form_class = StageForm
    template_name = 'events/stage_create.html'
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('events:event-list')
