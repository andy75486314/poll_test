from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns=[
    path('poll/',PollList.as_view(), name='poll_list'),
    path('poll/<int:pk>/',PollDetail.as_view(), name="poll_view"),
    path("poll/vote/<int:oid>/",PollVote.as_view()),
    path('poll/create/',PollCreate.as_view()),
    path("poll/<int:pk>/update/",PollUpdate.as_view()),
    path("poll/<int:pid>/create/",OptionCreate.as_view(), name="option_create"),
    path('option/<int:pk>',OptionEdit.as_view(), name='option_edit'),
    path("option/<int:pk>/delete/",OptionDelete.as_view(), name="option_delete"),
    path('<int:pk>/delete/',PollDelete.as_view(), name='poll_delete'),
]