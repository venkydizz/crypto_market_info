from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('market_summary/all/', views.market_summary_all, name='market_summary_all'),
    path('market_summary/for/', views.market_summary_for, name='market_summary_for'),
]
