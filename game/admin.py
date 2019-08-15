from django.contrib import admin
from .models import Dialogue, Answer, Location, Character, Narration

admin.site.register(Dialogue)
admin.site.register(Answer)
admin.site.register(Location)
admin.site.register(Character)
admin.site.register(Narration)
