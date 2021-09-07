from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, ListViewSet, CardViewSet, loginOauth

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'list', ListViewSet)
router.register(r'card', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('after_login/', loginOauth)
]
