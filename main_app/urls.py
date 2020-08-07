from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('city/post/', views.city_post, name="city_post"),
    path('city/', views.city_index, name='city_index'),
    path('city/<int:city_id>/', views.city_detail, name='city_detail'),
    path('city/<int:city_id>/new/', views.post_new, name='post_new'),
    path('profile/', views.profile, name="profile"),
    path('profile/update/', views.update, name="update_profile"),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/<int:post_id', views.post_delete, name='post_delete'),
]