from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns=[
    path('poll/',PollList.as_view()),
    path('poll/<int:pk>/',PollDetail.as_view()),
    path("poll/vote/<int:oid>/",PollVote.as_view()),
    path('create/',PollCreate.as_view()),
    path("poll/<int:pk>/update",views.PollUpdate.as_view())
]