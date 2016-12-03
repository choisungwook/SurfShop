#-*- encoding:utf-8 -*-
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.views import generic
from .models import Post, Subject
from django.views.generic.base import TemplateResponseMixin
from django.core.paginator import Paginator
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

def listtAll(request):
    return redirect(reverse('lecture:list', kwargs={'subject':1}))

class lectureListView(generic.ListView):
    # context_object_name = 'objects'
    template_name = 'lecture/list.html'
    model = Post
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(lectureListView, self).get_context_data(**kwargs)
        #모든 게시판의 카테고리를 구한다.
        context['subjects'] = Subject.objects.all()

        #subject가 있다면 게시판 리스트를 구한다.
        if self.kwargs['subject']:
            posts = Post.objects.filter(subject__id=self.kwargs['subject'])
            paginator = Paginator(posts, self.paginate_by)
            page = self.request.GET.get('page')

            if page is None:
                page = 1
                
            try:
                page_post = paginator.page(page)
            except PageNotAnInteger:
                page_post = paginator.page(1)
            except EmptyPage:
                page_post = paginator.page(paginator.num_pages)

            context['posts'] = page_post
        return context

    def get_queryset(self):
        queryset = super(lectureListView, self).get_queryset()
        subject = self.kwargs['subject']
        return  Post.objects.filter(subject__id=subject)
