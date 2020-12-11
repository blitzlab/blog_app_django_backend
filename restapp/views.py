from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import (
    IsAdminUser, DjangoModelPermissionsOrAnonReadOnly,
    BasePermission, SAFE_METHODS
)

class PostUserWritePermission(BasePermission):

    message = "Editing post is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostListView(generics.ListCreateAPIView):

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]

    queryset = Post.postobjects.all()

    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):

    permission_classes = [PostUserWritePermission,]

    queryset = Post.postobjects.all()
    
    serializer_class = PostSerializer
