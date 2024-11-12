from django.urls import path

from . import views

urlpatterns = [
    path(
        "test_analysis/", views.test_analysis, name="test_analysis"
    ),  # Temporary route for testing
    # We’ll add more routes here later, like webhook and other endpoints
]
