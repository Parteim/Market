from django.contrib import admin

from .models import (
    Product,
    PCCharacters,
    TVCharacters,
    MobilePhoneCharacters,
)


class PCCharactersAdmin(admin.TabularInline):
    model = PCCharacters


class TVCharactersAdmin(admin.TabularInline):
    model = TVCharacters


class MobilePhoneCharactersAdmin(admin.TabularInline):
    model = MobilePhoneCharacters


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    inlines = [PCCharactersAdmin, MobilePhoneCharactersAdmin, TVCharactersAdmin]