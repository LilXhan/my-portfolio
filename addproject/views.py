from django.shortcuts import render, redirect
from django.views.generic import View 
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import AddProjectForm
from .models import Project


class ProjectDetailView(LoginRequiredMixin, View):
    def get(self, request, id): 
        context = {
            'project': Project.objects.get(id=id),
        }
        return render(request, 'project/detail.html', context)

def view_404(request, exception=None):
    return redirect('index')

@login_required
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('projects')


class ProjectForm(LoginRequiredMixin, FormView):
    template_name = 'project/create.html'
    form_class = AddProjectForm

    def form_valid(self, form):
        cleaned_data = form.cleaned_data    
        project = Project.objects.create(**cleaned_data)
        project.save()
        return redirect('projects')


class ProjectView(LoginRequiredMixin, View):

    def get(self, request):
        tags = []
        tags_data = Project.objects.values_list('tags', flat=True)  
        for tag in tags_data:
            tag = tag.replace('[', '')
            tag = tag.replace("'", '')
            tag = tag.replace (' ', '')
            tag = tag.replace(']', '')
            tag = tag.split(',')
            tags.append(tag)
        context = {
            'data': Project.objects.all(),
            'tags': tags,
        }


        return render(request, 'project/projects.html', context)