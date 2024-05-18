from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artist_images/')
    category = models.ForeignKey(Category, related_name='artists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='songs/')
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
