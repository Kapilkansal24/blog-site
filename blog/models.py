from django.db import models
from users.models import UserModel
from datetime import datetime
# Create your models here.
class Blogs(models.Model):
    author = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    blog = models.TextField(max_length=2000)
    category = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now())

    def __str__(self):
        return f"{self.author}"