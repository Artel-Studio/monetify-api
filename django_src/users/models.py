from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='profile')
    has_goals_account = models.BooleanField(default=False)
    free_trial_starts = models.DateField(null=True, blank=True)
    free_trial_ends = models.DateField(null=True, blank=True)
    subscription_starts = models.DateField(null=True, blank=True)
    subscription_ends = models.DateField(null=True, blank=True)
    is_cat_creation_hint_was_shown = models.BooleanField(default=False)
    is_transaction_hint_was_shown = models.BooleanField(default=False)
    is_voice_hint_was_shown = models.BooleanField(default=False)
    is_goals_hint_was_shown = models.BooleanField(default=False)
    is_statistics_hint_was_shown = models.BooleanField(default=False)
    is_qr_hint_was_shown = models.BooleanField(default=False)
    currency = models.CharField(max_length=100)
    character = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username
