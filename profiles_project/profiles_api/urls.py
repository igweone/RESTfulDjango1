from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import HelloApiView
from .views import HelloViewSet
from .views import UserProfileViewSet


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet)#for modelViewsets you dont need base_name


urlpatterns = [
    url(r'^hello/', HelloApiView.as_view()),
    url(r'', include(router.urls))
   
]