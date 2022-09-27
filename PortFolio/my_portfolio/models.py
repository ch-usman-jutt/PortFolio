from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=3000)

    objects = models.Manager()

    def __str__(self):
        return self.subject