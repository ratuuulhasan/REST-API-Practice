from django.urls import path
from .views import SnippetList,SnippetDetail
urlpatterns = [
    path('sl/', SnippetList.as_view()),
    path('sl/<int:pk>', SnippetDetail.as_view()),
]