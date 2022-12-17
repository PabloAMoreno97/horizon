from rest_framework.views import APIView
from rest_framework.response import Response

from articlesApp.models.article import Article
from articlesApp.serializers.articleSerializer import ArticleSerializer


class ArticleDetailView(APIView):

    def get(self, request, pk=0):
        articles = Article.objects.all().values()
        if pk == 0:
            return Response(articles)
        else:
            for article in articles:
                if article['id'] == pk:
                    return Response(article)
            return Response({'Response': 'Article id ' + str(pk) + ' doesn\'t match'})
