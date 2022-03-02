from csv import excel
from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'update_at')
    exclude = ('created_at', 'update_at',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'number_in_stock',
                    'daily_rate', 'genre', 'date_created', 'update_at')
    exclude = ('date_created', 'update_at',)
    list_filter = ('title', 'genre')
    search_fields = ('title', 'genre')
    ordering = ('title', 'genre')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
