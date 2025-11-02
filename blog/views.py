from django.shortcuts import render
from django.urls import reverse_lazy

from .models import BlogPost

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blog'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content']
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blog:blog')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content']
    template_name = 'blog/blogpost_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:blogpost_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:blog')