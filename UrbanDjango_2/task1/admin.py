from django.contrib import admin
from .models import Buyer, Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    search_fields = ('title',)
    list_filter = ('size', 'cost')
    fields = [('title', 'size', 'cost'), 'description', 'age_limited', 'buyer']
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)
    list_filter = ('balance', 'age')
    list_per_page = 30