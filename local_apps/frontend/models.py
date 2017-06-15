from django.db import models

from ckeditor.fields import RichTextField

class Site(models.Model):
    name = models.CharField(max_length=144)
    logo = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True,
    )
    big_logo = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True,
    ) 
    short_logo = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True,
    )
    summary = RichTextField( blank=True )
    short_summary = RichTextField( blank=True )
    mision = RichTextField( blank=True )
    mision_img = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True,
    )
    vision = RichTextField( blank=True )
    vision_img = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        """ # """
        verbose_name = 'Asesalud Laboral'
        verbose_name_plural = 'Asesalud Laboral'

class Template(models.Model):
    HOME = 'frontend/index.html'
    COUNSELING = 'frontend/counseling.html'
    TRAINING = 'frontend/training.html'
    ASSESSMENT = 'frontend/assessment.html'
    CONTACT = 'frontend/contact.html'
    FORM_MESSAGE = 'frontend/contact_thanks.html'
    TEMPLATE_CHOICES = (
        (HOME, 'Inicio'),
        (COUNSELING, 'Asesorias'),
        (TRAINING, 'Capacitaciones'),
        (ASSESSMENT, 'Evaluaciones'),
        (CONTACT, 'Contacto'),
        (FORM_MESSAGE, 'Mensaje'),
    )
    name = models.CharField( max_length=144 )
    template = models.CharField(
        max_length=30,
        choices=TEMPLATE_CHOICES,
        default=HOME,
    )

    def __str__(self):
        return self.name

        




'frontend/index.html'