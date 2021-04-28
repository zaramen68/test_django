from django.urls import path

from .views import PollView, SinglePollView
# import poll.views

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', PollView.as_view()),
    path('articles/<int:pk>', SinglePollView.as_view())
]



# urlpatterns = [
#     url(r'^$',
#         app.views.PollListView.as_view(
#             queryset=Poll.objects.order_by('-pub_date')[:5],
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