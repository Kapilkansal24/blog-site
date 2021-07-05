from django.db import models

# Create your models here.
class UserModel(models.Model):
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    pic = models.ImageField(default=None, upload_to = "static/images")

    class Meta:
        ordering = ['firstname'] 
    
    def __str__(self):
        return f"{self.email}"
    