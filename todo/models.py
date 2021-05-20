from django.db import models

# Create your models here.
# class inheritance form django model class
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # override using name of item entered by user instead of the default 
    def __str__(self):
        return self.name

