"""Model to track the number of clicks made by a user"""
from datetime import datetime
from django.conf import settings
from django.db import models

# Create your models here.
class ClicksUser(models.Model):
    """Stored data for a user who clicks"""
    clicker = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    clicks = models.PositiveBigIntegerField(default=0)
    last_click = models.DateTimeField(default=datetime.now())
    click_speed = models.FloatField(default=0)

    def __str__(self) -> str:           #pylint: disable=invalid-str-returned
        return self.clicker.username    # pylint: disable=no-member
