from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Banner(models.Model):
    name = models.CharField( max_length=144 )
    description = RichTextField( blank=True )
    short = models.ImageField(
        upload_to='multimedia/banner/short/',
        null=True, 
        blank=True,
    )
    large = models.ImageField(
        upload_to='multimedia/banner/large/',
        null=True, 
        blank=True,
    )
    thumb = models.ImageField(
        upload_to='multimedia/banner/thumb/',
        null=True, 
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        """ """
        ordering = ['-created_at']