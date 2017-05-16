from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from blog.models import Post

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q


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


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schWord) |
                Q(description__icontains=schWord) | 
                Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

