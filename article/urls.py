from django.urls import path

from .views import PollView, SinglePollView, PollDetailView
# import poll.views

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', PollView.as_view()),
    path('articles/<int:pk>', PollDetailView.as_view(template_name='templates/app/polldetails.html'),
        name='detail'),
    # path('articles/<int:pk>', SinglePollView.as_view()),
    # path(r'^(?P<pk>\d+)/$',
    #     PollDetailView.as_view(
    #         template_name='app/polldetails.html'),
    #     name='detail'),
]



# urlpatterns = [
#     url(r'^$',
#         app.views.PollListView.as_view(
#             queryset=Question.objects.order_by('-poll_id'),
#             context_object_name='latest_poll_list',
#             template_name='app/index.html',),
#         name='home'),
#     url(r'^(?P<pk>\d+)/$',
#         app.views.PollDetailView.as_view(
#             template_name='app/details.html'),
#         name='detail'),
#     url(r'^(?P<pk>\d+)/results/$',
#         app.views.PollResultsView.as_view(
#             template_name='app/results.html'),
#         name='results'),
#     url(r'^(?P<poll_id>\d+)/vote/$', app.views.vote, name='vote'),
# ]