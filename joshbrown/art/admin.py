from django.contrib import admin

from .models import ArtPiece
from .models import Collection

# Register your models here.

admin.site.register(ArtPiece)
admin.site.register(Collection)