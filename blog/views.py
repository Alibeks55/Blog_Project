from .models import Post, Comment
from .serializers import PostSerializers, CommentSerializers
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadOnly
from .pagination import CustomPagination

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = CustomPagination
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    pagination_class = CustomPagination
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)








