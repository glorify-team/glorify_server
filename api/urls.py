from django.conf.urls import url, include
from rest_framework import routers

from api.views.mass_views import SongViewSet, AuthorViewSet, MassViewSet, MassMomentViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'songs', SongViewSet)
router.register(r'masses', MassViewSet)
router.register(r'mass-moments', MassMomentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
