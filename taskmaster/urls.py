from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from main.views import FileUploadView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from main.views import register
from main.viewsets.milestone import MilestoneViewSet
from main.viewsets.project import ProjectViewSet
from main.viewsets.task import TaskViewSet
from main.viewsets.configuration import ConfigurationViewSet

router = routers.DefaultRouter()
router.register(r"project", ProjectViewSet)
router.register(r"milestone", MilestoneViewSet)
router.register(r"task", TaskViewSet)
router.register(r"Configuration", ConfigurationViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("api/register/", register),
    path("upload/", FileUploadView.as_view(), name='file-upload'),
]
