# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from api.models import Song, Author, MassMoment, Mass

admin.site.register(Song)
admin.site.register(Author)
admin.site.register(MassMoment)
admin.site.register(Mass)
