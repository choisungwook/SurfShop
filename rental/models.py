from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class RentalCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name.encode('ascii', errors='replace')

    def get_absoulte_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class RentalProduct(models.Model):
    category = models.ForeignKey(RentalCategory, related_name='products')
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name.encode('ascii', errors='replace')

    def get_absoulte_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
