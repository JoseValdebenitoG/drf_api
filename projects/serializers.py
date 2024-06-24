

'''
    Ahora definimos que es lo que se mostrará al cliente
    según el metodo html usado (get, post, put, delete),
    esto creará los JSON que serán enviados al cliente
'''
# Importamos el modulo serializers 
from rest_framework import serializers
# Importamos nuestro modelo de base de datos
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        # definimos cual será el modelo, en este caso Project
        # que es nuestro modelo de base de datos
        model = Project
        # Ahora definimos los campos de la base de datos
        # en una tupla
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        # Definimos los campos de solo lectura
        read_only_fields = ('created_at',)
