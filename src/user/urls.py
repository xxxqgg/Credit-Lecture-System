from django.urls import path,include
from .views import (
    index_view,
    sign_out_view,
    login_view
)
app_name = 'user'
urlpatterns = [
    path('', index_view, name='index'),
    path('signout/', sign_out_view, name='signout'),
    path('login/', login_view, name='login')
]