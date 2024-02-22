from django.urls import path
from .views import *

urlpatterns = [
    path('p/', url_shortener, name='url_shortener'),
    path('<str:short_url>/', redirect_to_original, name='redirect_to_original'),
]