from django.urls import path
from . import views
from . views import PollList, PollDetail

urlpatterns = [
	path("", views.index, name="home"),
	path("polls/", views.polls_list, name="polls"),
	path("polls/<int:pk>/", views.polls_detail, name="polls_detail"),
	path("poll-list/", PollList.as_view(), name="poll-list"),
	path("poll-detail/<int:pk>/", PollDetail.as_view(), name="post-detail"),
]