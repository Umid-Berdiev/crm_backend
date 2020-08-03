from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from django.views import generic
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('ifis/', views.IFIList.as_view()),
    path('ifis/<int:pk>/', views.IFIDetail.as_view()),
    path('current_user/', views.get_current_user),
    path('users/create', views.CreateUserView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
