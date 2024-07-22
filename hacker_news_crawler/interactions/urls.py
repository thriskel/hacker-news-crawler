from django.urls import path
from .views import Interaction


urlpatterns = [
    path('', Interaction.as_view())
]
