
'''
    En este archivo definimos los viewset, que son los permisos
    para definir quien puede consultar nuestros datos
'''
# Importamos nuestro modelo de base de datos
from .models import Project
# Imporamos los modulos para viewset y permisos
from rest_framework import viewsets, permissions
# Importamos el serializer que creamos
from .serializers import ProjectSerializer


# Definimos las consultas
class ProjectViewSet(viewsets.ModelViewSet):
    # Consultamos todos los objetos
    queryset = Project.objects.all()
    '''
    Definimos los permisos
    usamos AllowAny para cualquier cliente y podemos usar
    IsAuthenticated para definir que solo un usuario autenticado
    pueda ingresar

    '''
    permission_classes = [permissions.AllowAny]
    # Definimos que serializer utilizamos
    serializer_class = ProjectSerializer
