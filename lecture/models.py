from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField

class Subject(models.Model):
    title=  models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='course')
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __unicode__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='module')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    def __unicode__(self):
        return '{}. {}'.format(self.order, self,title)

class content(models.Model):
    module = models.ForeignKey(Module, related_name='content')
    content_type = models.ForeignKey(ContentType,
                                    limit_choices_to={'model_in': {'text', 'video', 'image', 'file'}})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']

class ItemBase(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    crated_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='lecture/file')

class Image(ItemBase):
    image = models.ImageField(upload_to='lecture/image')
