from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('home/', views.home_view, name='home'),
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/modify_user/', views.modify_user_view, name='modify_user'),
    path('profile/update/', views.profile_update_view, name='profile_update'),  
    path('profile/change_password/', views.change_password_view, name='change_password'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('ciberseguridad/', views.ciberseguridad_view, name='ciberseguridad'),
    path('servers/', views.servers_view, name='servers'),
    path('pagina4/', views.pagina4_view, name='acerca'),
]
