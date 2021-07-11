from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# from django.contrib.auth.models import User


class Method(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/', default='default.png')
    description = models.TextField()
    score = models.IntegerField(default=0,
                                validators=[MaxValueValidator(5),
                                            MinValueValidator(0)
                                            ])
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)  # automatically populate field with the time suggestion was created.

    def __str__(self):
        # this function would enable us get the name in text when we call it from the shell programmatically
        return self.name

    def snippet(self):
        return self.description[:255] + "..."

    def str(self):
        return str(self.pk)


# class UserRating(models.Model):
    # method = models.ForeignKey(Method, related_name='ratings', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
