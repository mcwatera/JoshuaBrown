from django.shortcuts import render

# Create your views here.

from .models import ArtPiece

def index(request):
    latest_artworks = ArtPiece.objects.all()
    return render(request, "index.html", {'artworks': latest_artworks})
    
def contact(request):
    return render(request, "contact.html")