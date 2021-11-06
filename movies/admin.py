from django.contrib import admin
from .models import Movie, Actor, Review
# Register your models here.


class MovieAdmin (admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    list_display = ('name', 'likes', 'rate', 'production_date')
    fieldsets = (
        ['Main section', {'fields': ["name", 'description']}],
        [None, {"fields": ["likes", "rate", "production_date"]}],
        ["Actors and Poster", {"fields": ["actors", "poster"]}]
    )


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Review)
