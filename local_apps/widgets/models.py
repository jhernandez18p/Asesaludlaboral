from django.db import models
from local_apps.frontend.models import Template
from local_apps.multimedia.models import Banner
# Create your models here.

class Carousel(models.Model):
    POSITION_CHOICES = (
        ('HEADER','HEADER'),
        ('SECTION','SECTION'),
        ('FOOTER','FOOTER'),
    )
    name = models.CharField( max_length=144 )
    template = models.ForeignKey(
        blank=True, 
        null=True, 
        on_delete=models.CASCADE, 
        to='frontend.Template'
    )
    position = models.CharField(
        max_length=30,
        choices=POSITION_CHOICES,
        default='HEADER',
    )
    img = models.ManyToManyField( Banner )