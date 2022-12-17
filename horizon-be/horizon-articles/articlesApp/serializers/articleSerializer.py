from articlesApp.models.article import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'name', 'description', 'price', 'quantity']

    def create(self, validated_data):
        articleInstance = Article.objects.create(**validated_data)
        return articleInstance

    def to_representation(self, obj):
        article = Article.objects.get(id=obj.id)
        return {
            'id': article.id,
            'name': article.name,
            'description': article.description,
            'price': article.price,
            'quantity': article.quantity
        }
