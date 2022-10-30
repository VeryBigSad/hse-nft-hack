from django.urls import path

from backend.views import get_openai_data_view

urlpatterns = [
    path('openai', get_openai_data_view),
]
