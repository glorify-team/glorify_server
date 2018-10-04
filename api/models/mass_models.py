# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Author(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, verbose_name="Nome do autor")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Song(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=40, null=False, blank=False, verbose_name="Nome da música")
    lyrics = models.TextField(null=False, blank=False, verbose_name="Letra")
    author = models.ForeignKey(Author, null=True, blank=True, verbose_name="Autor")
    video_url = models.URLField(null=True, blank=True, verbose_name="Link do YouTube")

    def __unicode__(self):
        return '%s - %s' % (
            self.title,
            self.author.name if self.author is not None
            else 'Autor Desconhecido'
        )

    class Meta:
        verbose_name = 'Música'


class Mass(models.Model):
    description = models.TextField(null=True, blank=True, verbose_name="Sobre a missa")
    day = models.DateField(null=False, blank=False, verbose_name="Dia")

    def __unicode__(self):
        return 'Missa do dia %s' % self.day.strftime('%d/%m/%y')

    class Meta:
        verbose_name = 'Missa'


class MassMoment(models.Model):
    CHOICES = (
        ('EN', 'CANTO DE ENTRADA'),
        ('EP', 'EM NOME DO PAI'),
        ('AP', 'ATO PENITENCIAL'),
        ('GL', 'GLÓRIA'),
        ('SM', 'SALMO'),
        ('AL', 'ALELUIA'),
        ('OF', 'OFERTÓRIO'),
        ('ST', 'SANTO'),
        ('PC', 'PAZ DE CRISTO'),
        ('CD', 'CORDEIRO DE DEUS'),
        ('CM', 'COMUNHÃO'),
        ('PC', 'PÓS COMUNHÃO'),
        ('NS', 'ORAÇÃO DE NOSSA SENHORA'),
        ('CO', 'CANTO FINAL'),
        ('OT', 'OUTROS')
    )
    moment_name = models.CharField(max_length=2, choices=CHOICES, null=False, blank=False,
                                   verbose_name="Momento da Missa")
    mass = models.ForeignKey(Mass, null=True, related_name="mass_moments")
    reflection = models.TextField(null=True, blank=True, verbose_name="reflexão")
    songs = models.ManyToManyField(Song, verbose_name="Músicas do momento")

    def __unicode__(self):
        return 'momento %s da missa do dia %s' % \
               ([item for item in self.CHOICES if item[0] == self.moment_name][0][1], self.mass.day)

    class Meta:
        verbose_name = 'Momento da missa'
        verbose_name_plural = 'Momentos da missa'


# User post save signal: create token for DRF authentication


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
