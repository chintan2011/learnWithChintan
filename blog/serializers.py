# Telling REST Framework about our Posts model and how it should serialize the data.

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
                    'title',
                    'slug',
                    'author',
                    'tech_stack',
                    'github_url',
                    'updated_on',
                    'content',
                    'created_on',
                    'status'
                )