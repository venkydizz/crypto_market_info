from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('version/', views.version, name='version'),
    path('market_summary/all/', csrf_exempt(views.market_summary_all), name='market_summary_all'),
    path('market_summary/for/', csrf_exempt(views.market_summary_for), name='market_summary_for'),
]
