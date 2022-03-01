from django.urls import path
from . import views
urlpatterns = [
    # represente the root url
    path('', views.index, name='index'),
]
