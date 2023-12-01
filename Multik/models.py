from django.db import models

# Create your models here.
class Multik(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to = ' multiklar', null = True, blank = True )
    about = models.TextField(null=True)
    category = models.CharField(max_length = 255, null = True)
    file = models.FileField(upload_to = 'videos', null = True, blank = True)

    def __str__(self):
        return self.name

