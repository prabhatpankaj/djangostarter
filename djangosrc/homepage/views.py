# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404

def HomeView(request):
    return render_to_response('home.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

