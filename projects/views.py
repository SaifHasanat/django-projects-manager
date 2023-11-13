from django.shortcuts import render
from django.views.generic import ListView , CreateView
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectCreateForm

class ProjectListView(ListView ):
    model = Project
    template_name = 'projects/projects_list.html'
    context_object_name='projects'

class ProjectCreateView(CreateView):
    model = Project
    template_name='projects/ProjectsCreateView.html'
    form_class = ProjectCreateForm
    success_url = reverse_lazy('ProjectListView')







