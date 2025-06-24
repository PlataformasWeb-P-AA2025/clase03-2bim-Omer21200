from django.forms import ModelForm
from administrativo.models import Estudiante
from administrativo.models import Pais



class EstudianteForm(ModelForm): 
    class Meta:
        model = Estudiante 
        fields = ['nombre', 'apellido', 'cedula'] 

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'




