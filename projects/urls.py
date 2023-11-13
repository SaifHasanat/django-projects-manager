from django.urls import path ,include
from .views import ProjectListView,ProjectCreateView

urlpatterns = [
    path('projects',ProjectListView.as_view(),name='ProjectListView'),
    path('add_project', ProjectCreateView.as_view(), name='ProjectCreateView'),

]
