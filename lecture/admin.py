#-*- encoding:utf-8 -*-
from django.contrib import admin
from .models import Subject, Post
from django.db import models

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug":("title",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug":("title",)}
