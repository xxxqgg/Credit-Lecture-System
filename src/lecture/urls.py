from django.urls import path,include
from .views import (
    index_view,
    lecture_create_view,
    lecture_signup_view,
    detail_view,
    LectureViewSet,
    )
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', LectureViewSet)
app_name = 'lecture'
urlpatterns = [
    path('', index_view, name='index'),
    path('api', include(router.urls)),
    path('<int:id>/', detail_view,name='detail'),
    path('create',lecture_create_view,name='create'),
    path('lecture_signup', lecture_signup_view,name='signup'),

]