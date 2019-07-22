from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('entry/<int:pk>/detail/', views.entry_detail, name='entry_detail'),
    path('entry/new/', views.entry_new, name='entry_new'),
    path('entry/<int:pk>/edit/', views.entry_edit, name='entry_edit'),

]