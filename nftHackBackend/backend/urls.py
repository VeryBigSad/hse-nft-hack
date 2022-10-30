from django.urls import path

from backend.views import get_openai_data_view
from backend.views import download

urlpatterns = [
    path('openai', get_openai_data_view),
    path('file_by_data', download)
]
