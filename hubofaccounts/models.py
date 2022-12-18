from django.db import models
from django.utils.timezone import now
# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=12)
    desc = models.TextField()

    def __str__(self) :
        return self.name

class streviews(models.Model):
    sno = models.AutoField(primary_key= True)
    name = models.CharField(max_length=70)
    batch = models.CharField(max_length=70)
    review = models.TextField()
    timestamp = models.DateTimeField(default= now)

    def __str__(self) :
        return self.name + " - " + self.batch

class image(models.Model):
    Caption = models.CharField(max_length=300)
    Image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self) :
        return self.Caption

