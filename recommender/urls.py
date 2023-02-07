import imp
from django.urls import path
from . import views

urlpatterns = [
  path('', views.recommendphones, name='recommendphones'),
  #path('disphones/', views.DispPhones, name = 'display'),
  path('results/', views.results, name = 'results'),
]