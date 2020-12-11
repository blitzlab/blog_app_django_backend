from django.urls import path
from .views import PostListView, PostDetailView

app_name = "restapp"

urlpatterns=[
    path("", PostListView.as_view(), name="post_list"),
    path("detail/<int:pk>", PostDetailView.as_view(), name="post_detail"),
]
