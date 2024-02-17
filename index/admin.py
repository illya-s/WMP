from django.contrib import admin
from .models import Song, TypeMinistry, Ministry, SongMinistry

admin.site.register(Song)
admin.site.register(TypeMinistry)

class SongMinistryInline(admin.TabularInline):
    model = SongMinistry
    readonly_fields = ('id',)
    extra = 1

class MinistryAdmin(admin.ModelAdmin):
    inlines = [
        SongMinistryInline,
    ]
    list_display = ('name', 'date')
    list_filter = ('name',)
admin.site.register(Ministry, MinistryAdmin)
