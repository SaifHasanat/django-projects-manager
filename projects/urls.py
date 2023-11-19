from django.urls import path ,include
from .views import ProjectListView,ProjectCreateView,ProjectUpdateView ,TaskCreateView ,TaskUpdateView,TaskDeleteView ,TaskListView ,ProjectDeleteView

urlpatterns = [
    path('projects',ProjectListView.as_view(),name='ProjectListView'),
    path('add_project', ProjectCreateView.as_view(), name='ProjectCreateView'),
    path('projects/update/<int:pk>', ProjectUpdateView.as_view(), name='ProjectUpdateView'),
    path('projects/delete/<int:pk>', ProjectDeleteView.as_view(), name='ProjectDeleteView'),
    path('add_task', TaskCreateView.as_view(), name='TaskCreateView'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='TaskUpdateView'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='TaskDeleteView'),
    path('task_list', TaskListView.as_view(), name='TaskListView'),

]
