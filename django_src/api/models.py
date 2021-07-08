from django.db import models


class PromoCode(models.Model):
    free_days = models.PositiveIntegerField()
    new_character = models.CharField(max_length=250)
    code = models.CharField(max_length=255)
    new_users_only = models.BooleanField()
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.code
