from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


import unicodedata
from django.db.models import ImageField

class IdCard(ImageField):

    def __init__(self, *args, **kwargs):
        super(IdCard, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(IdCard, self).clean(*args, **kwargs)
        data.imagen = unicodedata.normalize('NFKD', data.imagen).encode('ascii', 'ignore')
        return data

class IdCard(models.Model):
    STATUS = {
        ('Published', 'Published'),
        ('Draft', 'Draft')
    }
    THEMES = {
        ('Light', 'Light'),
        ('Dark', 'Dark'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
    }
    status = models.CharField(max_length=12, choices=STATUS, default='Published')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    job = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    website = models.CharField(max_length=30, null=True, blank=True)
    qr_code = models.ImageField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True)
    theme = models.CharField(max_length=20, choices=THEMES, default='Light')
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(IdCard, self).save(*args, **kwargs)

        def __init__(self):
            return self.first_name