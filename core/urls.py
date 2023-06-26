from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('upload', views.upload, name='upload' ),
    path('signin', views.signin, name ='signin'),
    path('logout', views.logout, name ='logout'),
    path('settings', views.settings, name='settings')
];