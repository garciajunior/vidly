from django.urls import path
from . import views
app_name = 'movies'
urlpatterns = [
    # represente the root url
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
]
