from django.apps import AppConfig
from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
# Create your models here.


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        fields = ['title', 'release_year', 'number_in_stock', 'year',
                  'daily_rate', 'genre', 'date_created', 'update_at', ]
        allowed_methods = ['get']
        filtering = {
            'title': ('exact', 'startswith'),
            'year': ('exact', 'gt', 'gte', 'lt', 'lte'),
        }
