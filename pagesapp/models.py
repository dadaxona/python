from django.db import models

# Create your models here.
class Postlar(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    def __str__(self):
        return self.title

class Malumot(models.Model):
    praduct = models.CharField(max_length=200)
    soni = models.IntegerField()
    narx = models.IntegerField()
    def __str__(self):
        return self.praduct