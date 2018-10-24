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
def post_list(request):
    """
    List all post.
    """
    if request.method == 'GET':
        if request.data['slug'] != "":
            posts = Post.objects.all()
        else:
            posts = Post.objects.get(slug=request.data['slug'])
            
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def post_details(request):
    """
    Retrieve post details.
    """
    try:
        post = Post.objects.get(slug=request.data['slug'])
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
