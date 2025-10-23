from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("", views.EventListView.as_view(), name="event-list"),
    path("event/create/", views.EventCreateView.as_view(), name="event-create"),
    path("event/<int:pk>/", views.EventDetailView.as_view(), name="event-detail"),
    path("event/<int:pk>/update/", views.EventUpdateView.as_view(), name="event-update"),
    path("team/create/", views.TeamCreateView.as_view(), name="team-create"),
]