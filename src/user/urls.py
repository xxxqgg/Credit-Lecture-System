from django.urls import path,include
from .views import (
    index_view,
    signout_view,
)
app_name = 'user'
urlpatterns = [
    path('', index_view, name='index'),
    path('signout/',signout_view, name='signout'),
]