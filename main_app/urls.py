from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('stars/', views.stars_index, name='stars_index'),
  path('stars/<int:star_id>/', views.stars_detail, name='stars_detail'),
  path('stars/create/', views.StarCreate.as_view(), name='stars_create'),
  path('stars/<int:pk>/update/', views.StarUpdate.as_view(), name='stars_update'),
  path('stars/<int:pk>/delete/', views.StarDelete.as_view(), name='stars_delete'),
]