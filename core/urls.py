from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('upload', views.upload, name='upload' ),
    path('follow', views.follow, name='follow'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signin', views.signin, name ='signin'),
    path('like-post', views.like_post, name='like-post'),
    path('logout', views.logout, name ='logout'),
    path('search', views.search, name='search'),
    path('settings', views.settings, name='settings')
];


