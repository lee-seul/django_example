from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark


class BookmarkDV(DetailView):
    model = Bookmark


class BookmarkLV(ListView):
    model = Bookmark


