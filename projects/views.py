from django.shortcuts import render
from django.views.generic import ListView , CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy ,reverse
from .models import Project , Task
from .forms import ProjectCreateForm , ProjectUpdateForm ,TaskCreateForm

class ProjectListView(ListView ):
    model = Project
    template_name = 'projects/projects_list.html'
    context_object_name='projects'

class ProjectCreateView(CreateView):
    model = Project
    template_name='projects/ProjectsCreateView.html'
    form_class = ProjectCreateForm
    success_url = reverse_lazy('ProjectListView')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/ProjectUpdateView.html'
    form_class = ProjectUpdateForm
    def get_success_url(self):
        return reverse('ProjectUpdateView', args=[self.object.id])
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/delete_project.html'
    def get_success_url(self):
        return reverse ('ProjectListView')


class TaskCreateView(CreateView):
    model = Task
    fields=['description','project']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('ProjectUpdateView',args=[self.object.project.id])

class TaskUpdateView(UpdateView):
    model = Task
    fields=['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('ProjectUpdateView',args=[self.object.project.id])

class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('ProjectUpdateView',args=[self.object.project.id])
class TaskListView(ListView):
    model=Task
    template_name='task/TaskListView.html'
    context_object_name='tasks'









