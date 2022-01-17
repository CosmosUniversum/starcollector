from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('stars/', views.stars_index, name='stars_index'),
  path('stars/<int:star_id>/', views.stars_detail, name='stars_detail'),
  path('stars/<int:star_id>/add_photo/', views.add_photo, name='add_photo'),
  path('stars/create/', views.StarCreate.as_view(), name='stars_create'),
  path('stars/<int:pk>/update/', views.StarUpdate.as_view(), name='stars_update'),
  path('stars/<int:pk>/delete/', views.StarDelete.as_view(), name='stars_delete'),
  path('stars/<int:star_id>/add_exoplanet/', views.add_exoplanet, name='add_exoplanet'),
  path('exoplanets/<int:pk>/update/', views.ExoplanetUpdate.as_view(), name='exoplanet_update'),
  path('exoplanets/<int:pk>/delete/', views.ExoplanetDelete.as_view(), name='exoplanet_delete'),
]