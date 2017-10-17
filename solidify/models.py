import os
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


# Create your models here.
class ObjInput(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)
    file = models.FileField(upload_to="documents/%Y/%m/%d")
    added_time = models.DateTimeField(default=datetime.now())
    r = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)], default=0)
    g = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)], default=0)
    b = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)], default=0)
    thickness = models.FloatField(max_length=100.0, default=1.0)
    height = models.FloatField(max_length=100.0, default=1.0)

    def __str__(self):
        return self.name

    def get_filename(self):
        return os.path.basename(self.file.name)

    def get_mtl(self):
        return self.file.name.split(".")[0]+".mtl"

    def get_mtlname(self):
        return os.path.basename(self.get_mtl())

