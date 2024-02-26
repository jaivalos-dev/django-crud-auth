"""
URL configuration for djangocrud project.

Those are all the routes that the project need to enroute all views.
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path("tasks/create/", views.create_task, name="create_task"),
    path("tasks/<int:task_id>/", views.task_detail, name="task_detail"),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
