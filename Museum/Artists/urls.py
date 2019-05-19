from django.urls import path
from . import views

app_name = 'artists'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:artist_id>', views.detail, name='detail'),
    path('add', views.add, name='add'),
    path('save', views.save_artist, name='save_artist'),
    path('delete/<int:artist_id>', views.delete, name='delete'),
    path('edit/<int:artist_id>', views.edit, name='edit'),
    path('update/<int:artist_id>', views.update, name='update'),
]
