from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=200)
    img_url = models.CharField(max_length=400)
    description = models.CharField(max_length=400)    
    tags = models.CharField(max_length=100, choices=(
        ('python', 'Python'),
        ('css', 'CSS'),
        ('html', 'HTML'),
        ('javascript', 'Javascript'),
        ('etc', 'Etc')
    ))
    url_github = models.CharField(max_length=400)

    class Meta:
        db_table = 'projects'