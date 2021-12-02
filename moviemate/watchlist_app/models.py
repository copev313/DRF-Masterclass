from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=150)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamingPlatform,
                                 on_delete=models.CASCADE,
                                 related_name='watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(10)])
    comment = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList,
                                  on_delete=models.CASCADE,
                                  related_name='reviews')

    def __str__(self):
        return (f"{self.watchlist.title} | Rating: {self.rating}/10 "
                f"[{self.created.strftime('%m-%d-%Y')}]")
