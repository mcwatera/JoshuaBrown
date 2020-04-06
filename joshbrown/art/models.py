from django.db import models

# Create your models here.

class Collection(models.Model):
    coll_title = models.CharField(max_length=300)
    coll_desc = models.CharField(max_length=500)

class ArtPiece(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    
    