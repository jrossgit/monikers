from factory.django import DjangoModel

from app import models


class GameFactory():

    class Meta:
        model = "app.Game"


class CardFactory():

    class Meta:
        model = "app.Card"
