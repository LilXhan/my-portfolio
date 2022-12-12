from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='index')
]

handler404 = 'portfolio.views.view_404'
