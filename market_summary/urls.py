"""
URLs for market_summary app.
"""
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('ping/', csrf_exempt(views.ping), name='ping'),
    path('version/', csrf_exempt(views.version), name='version'),
    path('market_summary/all/', csrf_exempt(views.market_summary_all), name='market_summary_all'),
    path('market_summary/for/', csrf_exempt(views.market_summary_for), name='market_summary_for'),
]
