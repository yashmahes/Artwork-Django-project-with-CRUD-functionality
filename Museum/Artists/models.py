from django.db import models

# Create your models here.


class Artist(models.Model):
    Name = models.CharField(max_length=50)
    Birthplace = models.CharField(max_length=50)
    Born = models.CharField(max_length=50)
    Death = models.CharField(max_length=50)
    Movement = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Gallery(models.Model):
    Name = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    PostCode = models.CharField(max_length=50)
    country = models.CharField(max_length=15)
    director = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class ArtWork(models.Model):
    Name = models.CharField(max_length=30)
    artist_unique_code = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField()
    type_of_art = models.CharField(max_length=50)

    price = models.IntegerField()
    for_sale = models.CharField(max_length=3)
    gallery_code = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
