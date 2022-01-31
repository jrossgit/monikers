from app import models

from django.shortcuts import render


def game_list_view(request):
    return render(
        request,
        "game_list.html",
        context={
            "games": models.Game.objects.all()
        }
    )


def game_detail_view(request, game_id):
    game = models.Game.objects.get(id=game_id)

    return render(
        request,
        "game_detail.html",
        context={
            "game": game,
            "cards": game.cards.all(),
        }
    )
