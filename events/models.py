from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self): return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, unique=True)
    official_name = models.CharField(max_length=255, blank=True, null=True)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self): return self.name


class Venue(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self): return self.name


class Competition(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey(
        Sport,
        on_delete=models.PROTECT,
        related_name="competitions",
        db_column="_sport_foreignkey"
    )

    def __str__(self): return self.name


class Stage(models.Model):
    name = models.CharField(max_length=100)
    ordering = models.PositiveIntegerField(default=0)
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name="stages",
        db_column="_competition_foreignkey"
    )

    class Meta:
        ordering = ['ordering']
        unique_together = ['name', 'competition']

    def __str__(self): return f"{self.competition.name} - {self.name}"


class Event(models.Model):
    start_datetime = models.DateTimeField(db_index=True)
    status = models.CharField(
        max_length=20,
        choices=[('scheduled', 'scheduled'),
            ('played', 'played'),
            ('cancelled', 'cancelled')],
            default='scheduled')
    season = models.PositiveIntegerField(blank=True, null=True)
    stage = models.ForeignKey(
        Stage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="events",
        db_column="_stage_foreignkey"
    )
    home_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="home_events",
        db_column="_home_team_foreignkey"
    )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="away_events",
        db_column="_away_team_foreignkey"
    )
    venue = models.ForeignKey(
        Venue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="_venue_foreignkey"
    )
    home_goals = models.PositiveIntegerField(null=True, blank=True)
    away_goals = models.PositiveIntegerField(null=True, blank=True)
    winner = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wins",
        db_column="_winner_foreignkey"
    )
    result_details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start_datetime']
        indexes = [
            models.Index(fields=['start_datetime']),
            models.Index(fields=['season']),
        ]

    def __str__(self):
        home = self.home_team.name if self.home_team else 'N/A'
        away = self.away_team.name if self.away_team else 'N/A'
        return f"[{self.start_datetime.date()}] {home} vs {away}"
