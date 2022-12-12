from django.urls import path 
from . import views

urlpatterns = [
    path('projects/add/', views.ProjectForm.as_view(), name="create_project"),
    path('projects', views.ProjectView.as_view(), name='projects'),
    path('project/delete/<int:id>', views.delete_project, name="delete_project"),
    path('project/detail/<int:id>', views.ProjectDetailView.as_view(), name='detail_project')
]

handler404 = 'addproject.views.view_404'
