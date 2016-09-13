from django.db import models

# Create your models here.
class Asesorias(models.Model):

    name = models.CharField(max_length=140)
    title = models.CharField(max_length=140, blank=True)
    short_description = models.TextField(max_length=250)
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='asesorias')

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = ('Asesoría')
        verbose_name_plural = ('Asesorías')

        permissions = (
            ('can_add_asesoria','Can add asesoria'),
            ('can_edit_asesoria','Can edit asesoria'),
            ('can_delete_asesoria','Can delete asesoria'),
        )
