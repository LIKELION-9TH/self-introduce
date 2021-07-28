from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()

    def __self__(self):
        return self.title