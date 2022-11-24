from django.contrib import admin
from .models import Team, Venue, Event, Participation, Round, Revenue, Player


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Team)
admin.site.register(Venue)
admin.site.register(Event, PostAdmin)
admin.site.register(Participation)
admin.site.register(Round)
admin.site.register(Revenue)
admin.site.register(Player)
