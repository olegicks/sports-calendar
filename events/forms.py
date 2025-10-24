from django import forms
from .models import Event, Team, Venue, Sport, Competition, Stage


class EventForm(forms.ModelForm):
    start_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Date & Time"
    )

    class Meta:
        model = Event
        fields = [
            'start_datetime',
            'status',
            'season',
            'stage',
            'home_team',
            'away_team',
            'venue'
        ]


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'start_datetime',
            'status',
            'season',
            'stage',
            'home_team',
            'away_team',
            'venue',
            'home_goals',
            'away_goals',
            'winner',
            'result_details'
        ]


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'slug', 'official_name', 'abbreviation', 'country_code']


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'city']


class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ['name', 'slug']


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['id', 'name', 'sport']


class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['name', 'ordering', 'competition']
