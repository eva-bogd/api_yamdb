from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet,
                    AuthViewSet, TitleViewSet, GenreViewSet, CategoryViewSet, ReviewViewSet, CommentViewSet,)

router_api_v1 = DefaultRouter()

router_api_v1 = DefaultRouter()
router_api_v1.register(r'^users', UserViewSet)
router_api_v1.register(r'^auth', AuthViewSet)
router_api_v1.register(r'^titles', TitleViewSet, basename='titles')
router_api_v1.register(r'^genres', GenreViewSet, basename='genres')
router_api_v1.register(r'^categories', CategoryViewSet, basename='categories')
router_api_v1.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews')
router_api_v1.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
]
