from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=40)

    def __str__(self):
        return '%s - %s - %s' % (self.model, self.year, self.color)

    def save(self, *args, **kwargs):
        self.model = self.model.upper()
        self.year = self.year.upper()
        super(Car, self).save(*args, **kwargs)
