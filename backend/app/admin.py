from app import models

from django.contrib import admin

# Register your models here.
@admin.register(models.Game)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Card)
class AuthorAdmin(admin.ModelAdmin):
    pass
