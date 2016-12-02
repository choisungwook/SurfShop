#-*- encoding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from embed_video.fields import EmbedVideoField

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "블로그 카테고리"
        verbose_name_plural = "블로그 카테고리들"

class Post(models.Model):
    subject = models.ForeignKey(Subject, related_name='subjects')
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200)
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)
    video = EmbedVideoField()

    def __unicode__(self):
        return self.title

    def get_markdown(self):
        markdownify = import_string(settings.MARKDOWNX_MARKDOWNIFY_FUNCTION)
        return markdownify(self.body)

    class Meta:
        verbose_name = "블로그 내용"
        verbose_name_plural = "블로그 내용들"
        ordering = ['-created_in']
