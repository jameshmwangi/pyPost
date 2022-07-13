from dataclasses import fields
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['title','content','date_posted','authour']

class CreatePostSerializer(serializers.ModelSerializer):
    content=serializers.CharField(required=True)
    class Meta:
        model =Post
        fields=['title','content','authour','date_posted']
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

class EditPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['title','content']

    def update(self,instance,validated_data):
        return super().update(instance,validated_data)
