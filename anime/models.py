from django.db import models

class Anime(models.Model):
    url_video = models.TextField(blank=True, null=True)
    nombre_anime = models.TextField(blank=True, null=True)
    url_imagen = models.TextField(blank=True, null=True)
    urls_capitulos = models.TextField(blank=True, null=True)
    urls_adicionales = models.TextField(blank=True, null=True)
    urls_video = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'anime'
