# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from post.models import Post
from post.serializers import PostSerializer

# Create your views here.

@csrf_exempt
def post_list(request,slug=""):
    """
    List all post.
    """
    if request.method == 'GET':
        if slug == "":
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            posts = Post.objects.get(slug=slug)
            serializer = PostSerializer(posts)
            return JsonResponse(serializer.data)
        
