from app.views import TodoList, AddTask, DeleteTask, Login, RegisterPage
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [
    path("login/", Login.as_view(), name='login' ),
    path("logout/", LogoutView.as_view(next_page= 'login'), name='logout' ),
    path("register/", RegisterPage.as_view(), name='register' ),
    path("", TodoList.as_view(), name='todos' ),
    path("add/", AddTask.as_view(), name='add' ),
    path("delete/<int:pk>", DeleteTask.as_view(), name='delete' ),
    path("admin/", admin.site.urls, name='Home'),
]
