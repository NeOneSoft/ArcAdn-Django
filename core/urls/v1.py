from django.conf.urls import url, include
from rest_framework import routers

from core.views import UserViewSet
from dna.views import DnaViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'POST/mutation', DnaViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]