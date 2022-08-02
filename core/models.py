from secrets import choice
from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)

    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)


class Que(models.Model):
    STATUS_CHOICES = (
        (1, 'Queing'),
        (2, 'Done'),
        (3, 'Cancled'),
    )
    user_id = models.IntegerField()
    store_id = models.IntegerField()
    is_hot_que = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)
