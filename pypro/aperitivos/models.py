from django.db import models
from django.urls import reverse


class Video(models.Model):

    slug = models.SlugField(max_length=32)
    titulo = models.CharField(max_length=32)
    vimeo_id = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))

    def __str__(self) -> str:
        return f'{self.titulo}'
