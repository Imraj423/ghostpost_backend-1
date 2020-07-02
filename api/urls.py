from django.conf.urls import include,url

from api.views import GhostPostViewSet
from rest_framework import routers



router = routers.DefaultRouter()

router.register(r'posts', GhostPostViewSet, basename='post')

urlpatterns = [
    url(r"^api/", include(router.urls))
]