from rest_framework.routers import DefaultRouter

from apps.series.api.serializers import *
from apps.series.api.viewsets import *

router = DefaultRouter()

router.register(r'series',serieViewset, basename = 'series')
router.register(r'temporadas',temporadaViewset, basename = 'temporadas')

urlpatterns = router.urls
