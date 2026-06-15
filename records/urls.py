from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('darta/', views.darta_list, name='darta_list'),
    path('chalan/', views.chalan_list, name='chalan_list'),

    path('darta/edit/<int:id>/', views.edit_darta, name='edit_darta'),
    path('darta/delete/<int:id>/', views.delete_darta, name='delete_darta'),

    path('chalan/edit/<int:id>/', views.edit_chalan, name='edit_chalan'),
    path('chalan/delete/<int:id>/', views.delete_chalan, name='delete_chalan'),

    path('export-darta/', views.export_darta_excel, name='export_darta'),
    path('export-chalan/', views.export_chalan_excel, name='export_chalan'),

    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.create_user, name='create_user'),

    path('users/edit/<int:id>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:id>/', views.delete_user, name='delete_user'),
]