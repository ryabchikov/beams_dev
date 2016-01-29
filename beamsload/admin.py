from django.contrib import admin

# Register your models here.

from .models import Beam, Point

class PointsInline(admin.StackedInline):
    model = Point
    extra = 3

class BeamsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['beam_name']}),
        ('Satellite name', {'fields': ['satellite_name']}),
    ]
    inlines = [PointsInline]
    



admin.site.register(Beam, BeamsAdmin)
admin.site.register(Point)
