from django.shortcuts import render
from rest_framework.generics import  get_object_or_404, GenericAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from django.views.generic import ListView, DetailView
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Poll, Question, Answer, Respondent, Author
from .serializers import ArticleSerializer, PollSerializer, QuestionSerializer
import json

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

class PollView(ListModelMixin, GenericAPIView):
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

##################################################################

class PollListView(ListView):
    """Renders the home page, with a list of all polls."""
    model = Poll

    def get_context_data(self, **kwargs):
        context = super(PollListView, self).get_context_data(**kwargs)
        context['title'] = 'Polls'
        context['year'] = datetime.now().year
        return context

class PollDetailView(DetailView):
    """Renders the poll details page."""
    model = Poll

    def get_context_data(self, **kwargs):
        context = super(PollDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Poll'
        context['year'] = datetime.now().year
        return context

class PollResultsView(DetailView):
    """Renders the results page."""
    model = Poll

    def get_context_data(self, **kwargs):
        context = super(PollResultsView, self).get_context_data(**kwargs)
        context['title'] = 'Results'
        context['year'] = datetime.now().year
        return context

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def vote(request, poll_id):
    """Handles voting. Validates input and updates the repository."""
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app/details.html', {
            'title': 'Poll',
            'year': datetime.now().year,
            'poll': poll,
            'error_message': "Please make a selection.",
    })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('app:results', args=(poll.id,)))

# @login_required
# def seed(request):
#     """Seeds the database with sample polls."""
#     samples_path = path.join(path.dirname(__file__), 'samples.json')
#     with open(samples_path, 'r') as samples_file:
#         samples_polls = json.load(samples_file)

#     for sample_poll in samples_polls:
#         poll = Poll()
#         poll.text = sample_poll['text']
#         poll.pub_date = timezone.now()
#         poll.save()

#         for sample_choice in sample_poll['choices']:
#             choice = Choice()
#             choice.poll = poll
#             choice.text = sample_choice
#             choice.votes = 0
#             choice.save()

#     return HttpResponseRedirect(reverse('app:home'))


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