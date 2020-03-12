from django.urls import include, path
from rest_framework import routers
from .views import TaskViewSet, WBSViewSet


router = routers.DefaultRouter()
router.register('task', TaskViewSet)
router.register('wbs', WBSViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
] 
