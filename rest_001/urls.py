from rest_framework import routers
from .api import TaskViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, 'tasks')
urlpatterns = router.urls