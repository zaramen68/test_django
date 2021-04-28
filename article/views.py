from django.shortcuts import render
from rest_framework.generics import get_object_or_404, GenericAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Poll, Question, Answer, Respondent
from .serializers import ArticleSerializer, PollSerializer, QuestionSerializer


class ArticleView( ListModelMixin, GenericAPIView):
    queryset= Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs )

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
#############################################################################

class PollView( ListModelMixin, GenericAPIView):
    queryset= Poll.objects.all()
    serializer_class = PollSerializer

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs )

    # def perform_create(self, serializer):
    #     author = get_object_or_404(Author, id=self.request.data.get('author_id'))
    #     return serializer.save(author=author)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SinglePollView(RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer



    # def post(self, request):
    #     article = request.data.get('article')

    #     serializer = ArticleSerializer(data = article)
    #     if serializer.is_valid(raise_exeption=True):
    #         article_saved = serializer.save()
    #     return Response({"success": "Article '{}' created successfully".format(article_saved.title)})


    # def put(self, request, pk):
    #     saved_article = get_object_or_404(Article.objects.all(), pk=pk)
    #     data = request.data.get('article')
    #     serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({
    #         "success": "Article '{}' updated successfully".format(article_saved.title)
    #     })

    # def delete(self, request, pk):
    #     # Get object with this pk
    #     article = get_object_or_404(Article.objects.all(), pk=pk)
    #     article.delete()
    #     return Response({
    #         "message": "Article with id `{}` has been deleted.".format(pk)
    #     }, status=204)