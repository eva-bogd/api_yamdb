from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TitleViewSet, ReviewViewSet, CommentViewSet

router = DefaultRouter()

router.register('titles', TitleViewSet, basename='titles')
router.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews')
router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
]