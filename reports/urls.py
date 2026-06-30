from django.urls import path
from . import views

urlpatterns = [
    path("download/<int:inspection_id>/", views.download_report, name="download_report"),
]