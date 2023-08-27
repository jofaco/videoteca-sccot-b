from django.db import models

# Create your models here.
class Serie(models.Model):
    serie = models.CharField('Nombre de la serie', max_length=100)
    description = models.TextField('Descripción de la serie')
    quantity = models.IntegerField('Cantidad de videos', default=0)


    class Meta:
        """Meta definition for Serie."""

        verbose_name = 'Nombre de la serie'
        verbose_name_plural = 'Nombres de series'

    def __str__(self):
        """Unicode representation of Serie."""
        return self.serie
    
class Temporada(models.Model):
    temporada = models.CharField('Nombre de la Temporada', max_length=50)
    temporada_letras = models.CharField('Temporada en letras', max_length=50, null=True)
    temporada_numero = models.IntegerField('Temporada en numeros')
    description = models.TextField('Descripción de la temporada')
    create_date = models.DateField('Fecha de creación', auto_now=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name='Serie')
    class Meta:
        """Meta definition for Temporada."""

        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'

    def __str__(self):
        """Unicode representation of Temporada."""
        return self.temporada