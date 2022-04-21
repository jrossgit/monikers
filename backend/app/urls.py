"""coasters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("games", views.game_list_view, name="game_list_view"),
    path("games/new", views.game_create_view, name="game_create_view"),
    path("games/<uuid:game_id>", views.game_detail_view, name="game_detail_view"),
    path("htmx/new_card", views.new_card_htmx_view, name="new_card_htmx_view"),
]


urlpatterns.append(
    path("admin/", admin.site.urls),
)
