from django.db import models

# Create your models here.
class User(models.Model):
    TOKYO = "東京"
    OSAKA = "大阪"
    NAGOYA = "名古屋"
    SENDAI = "仙台"
    SAPPORO = "札幌"
    AREA_CHOICES = [
        (TOKYO, 'tokyo'),
        (OSAKA, 'osaka'),
        (NAGOYA, 'nagoya'),
        (SENDAI, 'sendai'),
        (SAPPORO, 'sapporo')
    ]


    age = models.CharField(max_length=5)
    area = models.CharField(
        choices=AREA_CHOICES,
        default = "TOKYO"
    )
    gender = models.PositiveIntegerField()
    email = models.EmailField()
    password = models.CharField()
    isPaid = models.BooleanField()

class Movie(models.Model):
    name = models.CharField()
    url = models.CharField()
    isPublished = models.BooleanField()
    probability = models.DecimalField()

class MyMovie(models.Model):
    users_id = models.ForeignKey("User", on_delete=models.CASCADE)
    movie_id = models.ForeignKey("Movie",on_delete=models.CASCADE)