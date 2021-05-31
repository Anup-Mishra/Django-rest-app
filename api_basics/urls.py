from django.urls import path
from django.urls.conf import include
from .views import ArticleApiView, ArticleDeatilApiView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',ArticleViewSet,basename='article')

urlpatterns = [
    path('article/',ArticleApiView.as_view()),
    path('detail/<int:pk>/',ArticleDeatilApiView.as_view()),
    path('viewsets/',include('router.urls')),
    path('viewsets/<int:pk>/',include('router.urls')),
]