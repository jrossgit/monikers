import uuid

from django.shortcuts import render, redirect

from app import forms, models
from app.forms import NewGameForm


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


def game_create_view(request):

    if request.method == "GET":
        return render(request, "game_create.html", context={"form": forms.NewGameForm()})
    elif request.method == "POST":
        form = NewGameForm(request.POST)
        form.save()
        return redirect("game_list_view")


def home_view(request):
    return redirect("game_list_view")


def new_card_htmx_view(request):

    return render(
        request,
        "htmx/card_new_form.html"
    )
