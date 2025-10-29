from django.test import TestCase
from django.urls import reverse
from .models import Event, Sport, Competition, Stage, Team
import datetime


class EventViewTests(TestCase):

    def setUp(self):
        self.sport = Sport.objects.create(name="Test Sport", slug="test-sport")
        self.competition = Competition.objects.create(name="Test Comp", sport=self.sport)
        self.stage = Stage.objects.create(name="Test Stage", competition=self.competition)
        self.team1 = Team.objects.create(name="Team A", slug="team-a")
        self.team2 = Team.objects.create(name="Team B", slug="team-b")

        self.event = Event.objects.create(
            start_datetime=datetime.datetime(2025, 11, 1, 12, 0, tzinfo=datetime.timezone.utc),
            stage=self.stage,
            home_team=self.team1,
            away_team=self.team2
        )


    def test_event_list_view_loads(self):
        response = self.client.get(reverse('events:event-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_list.html')


    def test_event_list_displays_event(self):
        response = self.client.get(reverse('events:event-list'))
        self.assertContains(response, "Team A")
        self.assertContains(response, "Team B")


    def test_event_create_view_get(self):
        response = self.client.get(reverse('events:event-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_create.html')


    def test_event_create_view_post(self):
        new_event_data = {
            'start_datetime': '2025-12-01T14:00',
            'status': 'scheduled',
            'stage': self.stage.pk,
            'home_team': self.team1.pk,
            'away_team': self.team2.pk,
        }

        initial_event_count = Event.objects.count()
        response = self.client.post(reverse('events:event-create'), data=new_event_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('events:event-list'))

        self.assertEqual(Event.objects.count(), initial_event_count + 1)
        new_event = Event.objects.latest('created_at')
        self.assertEqual(new_event.home_team, self.team1)
