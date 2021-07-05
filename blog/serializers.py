from rest_framework import serializers
from .models import Blogs

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogs # the model whose data you will share
        fields = ['title', 'blog', 'category']
