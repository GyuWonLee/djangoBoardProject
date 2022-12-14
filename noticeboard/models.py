from django.db import models
from django.utils.timezone import now


# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=100)
    contents = models.CharField(max_length=2000)
    writeDate = models.DateTimeField(default=now, editable=False)
    writeId = models.CharField(max_length=50)

    def __str__(self):
        return self.title

