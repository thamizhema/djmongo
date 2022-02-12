from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout/',views.logout, name="logout"),
    path('add_post/', views.addPost, name="add_post"),
    path('get_post/', views.getPost, name="get_post"),
    path('delete_post/<str:id>/', views.delete, name="delete_post"),
    path('update_post/<str:id>/', views.updateForm, name="update_post"),
    path('updating/<str:id>/', views.update, name="updating"),
    path('file_upload/', views.fileUpload, name="file_upload"),
    path('img_view/', views.fileView, name="img_view"),
    path('send_email/', views.sendEmail, name ='send_email'),
   
    
]
