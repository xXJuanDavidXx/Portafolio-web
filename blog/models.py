from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(default=datetime.date.today)
    category = models.ManyToManyField(Category, default=None)  # muchos posts pueden estar relacionados a muchas categorias

    def __str__(self) -> str:
        return self.title
