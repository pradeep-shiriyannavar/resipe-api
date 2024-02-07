"""
Seriazers for recipe API
"""
from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Seriazer for recipe"""

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minute', 'price', 'link'
            ]
        read_only_fields = ['id']

class RecipeDetailSerializer(RecipeSerializer):
    """Serialzer for recipe detail view"""


    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
