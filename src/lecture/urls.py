from django.urls import path,include
from .views import (
    index_view,
    lecture_create_view,
    detail_view,
    LectureViewSet,
    )
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', LectureViewSet)
app_name = 'lecture'
urlpatterns = [
    path('', index_view),
    path('api', include(router.urls)),
    path('<int:id>/', detail_view),
    path('create',lecture_create_view),
]