from django import forms
from .models import Event

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