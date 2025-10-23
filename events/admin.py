from django.contrib import admin
from .models import Sport, Team, Venue, Competition, Stage, Event


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "abbreviation", "country_code")
    search_fields = ("name", "slug", "official_name")
    list_filter = ("country_code",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "city")
    search_fields = ("name", "city")


class StageInline(admin.TabularInline):
    model = Stage
    extra = 1
    ordering = ("ordering",)


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sport")
    list_filter = ("sport",)
    search_fields = ("name", "id")
    inlines = [StageInline]


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "competition", "ordering")
    list_filter = ("competition__sport", "competition")
    search_fields = ("name", "competition__name")
    list_select_related = ("competition",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "display_title", "competition_name", "stage", "start_datetime", "status")
    list_filter = ("status", "stage__competition__sport", "start_datetime")
    search_fields = ("home_team__name", "away_team__name", "stage__name")
    list_select_related = ("stage__competition", "home_team", "away_team")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-start_datetime",)

    def display_title(self, obj):
        home = obj.home_team.name if obj.home_team else "N/A"
        away = obj.away_team.name if obj.away_team else "N/A"
        return f"{home} vs {away}"
    display_title.short_description = "Match"

    @admin.display(description="Competition", ordering="stage__competition")
    def competition_name(self, obj):
        return obj.stage.competition if obj.stage else None
