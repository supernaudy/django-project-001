from django.urls import path
from auth_001 import views

urlpatterns = [
    # AUTH VIEWS
    path('', views.index, name='index'),
    path('signout/', views.signout, name='signout'),
    #TASK VIEWS
    path('tasks/', views.tasks, name='tasks'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/done/<int:task_id>/', views.mark_as_done, name='mark_as_done'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]