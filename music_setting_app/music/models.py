from django.db import models
from .until import upload_avatar_path


# Create your models here.
# Chức nghiệp: Nghệ sĩ, Ca sĩ, Nhạc sĩ,...
class Profession(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Tên nghệ sĩ
class Singer(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    professions = models.ManyToManyField(Profession, related_name='singers', blank=True)
    description = models.TextField(null=True)
    avatar = models.ImageField(blank=True, default="", upload_to=upload_avatar_path, null=True)

    def __str__(self):
        return self.name


# Thương hiệu
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Đất nước
class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Bài hát
class Song(models.Model):
    name = models.CharField(max_length=250)
    release = models.DateField()
    time = models.IntegerField()
    lyric = models.TextField()
    description = models.TextField()
    file_mp3 = models.CharField(max_length=250)
    categories = models.ManyToManyField(Category, blank=True)
    countries = models.ManyToManyField(Country, blank=True)
    singers = models.ManyToManyField(Singer, blank=True)
