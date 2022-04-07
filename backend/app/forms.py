from django.forms import ModelForm
from app import models


class NewGameForm(ModelForm):
    class Meta:
        model = models.Game
        fields = ["name"]
