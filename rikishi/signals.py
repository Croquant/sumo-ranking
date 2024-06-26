from django.db.models.signals import post_save
from django.dispatch import receiver

from glicko.models import Glicko

from .models import Rikishi


@receiver(post_save, sender=Rikishi)
def create_elo_for_image(sender, instance, created, **kwargs):
    if created:
        Glicko.objects.create(rikishi=instance)
