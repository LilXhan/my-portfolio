from django.shortcuts import render, redirect
from django.views.generic import View

class Index(View):
    
    def get(self, request):
        return render(request, 'index.html')


def view_404(request, exception=None):
    return redirect('index')