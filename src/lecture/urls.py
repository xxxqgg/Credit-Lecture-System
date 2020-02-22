from django.urls import path,include
from .views import (
    index_view,
    lecture_create_view,
    lecture_signup_view,
    detail_view,
    LectureViewSet,
    lecture_draw_view
    )


app_name = 'lecture'
urlpatterns = [
    path('', index_view, name='index'),
    path('<int:id>/', detail_view,name='detail'),
    path('create',lecture_create_view,name='create'),
    path('<int:lecture_id>/signup/', lecture_signup_view,name='signup'),
    path('<int:lecture_id>/draw', lecture_draw_view, name='draw')
]
