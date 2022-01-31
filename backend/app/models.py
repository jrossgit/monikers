from django.db import models


# Create your models here.
class Game(models.Model):

    id = models.fields.UUIDField(verbose_name="Game UUID", primary_key=True)


class Card(models.Model):

    id = models.fields.UUIDField(verbose_name="Card UUID", primary_key=True)
    title_text = models.fields.CharField(max_length=256)
    help_text = models.fields.CharField(max_length=512, null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="cards")
