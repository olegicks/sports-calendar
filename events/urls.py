from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("", views.EventListView.as_view(), name="event-list"),
    path("event/create/", views.EventCreateView.as_view(), name="event-create"),
]