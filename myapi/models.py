from django.db import models

# Create your models here.

class Cart(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()

    def __str__(self):
        return self.item_name

