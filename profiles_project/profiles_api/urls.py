from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import HelloApiView
from .views import HelloViewSet


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    url(r'^hello/', HelloApiView.as_view()),
    url(r'', include(router.urls))
   
]