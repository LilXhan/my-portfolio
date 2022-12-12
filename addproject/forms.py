from django import forms

class AddProjectForm(forms.Form):

    options = [
        ('python', 'Python'),
        ('css', 'CSS'),
        ('html', 'HTML'),
        ('javascript', 'Javascript'),
        ('etc', 'Etc')
    ]

    title = forms.CharField(max_length=200, label='Nombre del proyecto', required=True)
    img_url = forms.CharField(max_length=400, label='URL de la imagen del proyecto', required=True)
    description = forms.CharField(max_length=400, label='Descripción del proyecto', required=True)
    tags = forms.MultipleChoiceField(
        label='¿Cuáles son las herramientas que usaste en este proyecto?', choices= options, widget=forms.CheckboxSelectMultiple, required=True
    )
    url_github = forms.CharField(max_length=400, label='URL del repositorio en github', required=True)
