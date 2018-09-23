# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from api.models.mass_models import Song, Author, MassMoment, Mass


class MassMomentInline(admin.StackedInline):
    model = MassMoment
    extra = 1


class MassAdmin(admin.ModelAdmin):
    fields = ['description', 'day']
    inlines = [MassMomentInline]


admin.site.register(Song)
admin.site.register(Author)
admin.site.register(MassMoment)
admin.site.register(Mass, MassAdmin)
