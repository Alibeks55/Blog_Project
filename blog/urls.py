from django.urls import path
from .views import PostViewSet, CommentViewSet
from .constants import LIST_CREATE, RETRIEVE_UPDATE_DESTROY

urlpatterns = [
    path('posts/', PostViewSet.as_view(LIST_CREATE)),
    path('posts/<int:id>/', PostViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),

    path('comments/', CommentViewSet.as_view(LIST_CREATE)),
    path('comments/<int:id>/', CommentViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
]