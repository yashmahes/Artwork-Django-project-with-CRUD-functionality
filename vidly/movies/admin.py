from django.contrib import admin
from .models import Artist, Gallery, ArtWork
# Register your models here.

admin.site.register(Artist)
admin.site.register(Gallery)
admin.site.register(ArtWork)
