from django.urls import path
from .views import Crawler


urlpatterns = [
    path('', Crawler.as_view())
]
