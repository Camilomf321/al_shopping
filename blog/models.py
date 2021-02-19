from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='articles/%Y/%m/%d/', blank=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blog:blog_detail',
                       args=[self.publish.year, self.publish.month, self.publish.day, self.slug, self.id])

    def __str__(self):
        return 'Articulo '.format(self.id)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
