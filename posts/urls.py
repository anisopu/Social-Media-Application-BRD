from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    
]
