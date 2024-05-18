from django.urls import path
from .views import CategoryListCreate, CategoryDetail, SongList

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('songs/', SongList.as_view(), name='song-list'),
]
