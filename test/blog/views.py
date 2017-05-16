from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from blog.models import Post


class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2
    

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


class PostDV(DetailView):
    model = Post


