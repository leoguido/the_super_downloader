from django.urls import include, path
from rest_framework import routers
from api_rest import views

router = routers.DefaultRouter()
router.register(r'users', views.UserApiView)
router.register(r'formats', views.FormatApiView)
router.register(r'downloads', views.DownloadSerializer)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]