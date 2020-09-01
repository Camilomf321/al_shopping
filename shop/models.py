from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=70, verbose_name='Nombre de la Categoria')
    slug = models.SlugField(verbose_name='Slug de la Categoria')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    is_menu = models.BooleanField(default=False, verbose_name='¿Hace parte del menú de Navegacion?')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('-created',)

    def __str__(self):
        return self.name


class ProductAvailableManager(models.Manager):
    def get_queryset(self):
        return super(ProductAvailableManager, self).get_queryset().filter(available=True)


class ProductFeaturedManager(models.Manager):
    def get_queryset(self):
        return super(ProductFeaturedManager, self).get_queryset().filter(featured=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria del Producto')
    name = models.CharField(max_length=200, verbose_name='Nombre del Producto')
    slug = models.SlugField(verbose_name='Slug del Producto')
    description = models.TextField(verbose_name='Descripción del Producto')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio del Producto')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Imagen del Producto')
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Peso del Producto (en Kg)', blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Altura del Producto (en cm)', blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Anchura del Producto (en cm)', blank=True, null=True)
    available = models.BooleanField(default=True, verbose_name='¿Está disponible el Producto?')
    featured = models.BooleanField(default=False, verbose_name='¿Producto Featured?')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    product_available = ProductAvailableManager()
    product_featured = ProductFeaturedManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
