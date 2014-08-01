from django.contrib import admin


# Register your models here.
from mood.models import *

admin.site.register(Listener)
admin.site.register(Song)
admin.site.register(Mood)
admin.site.register(Movie)