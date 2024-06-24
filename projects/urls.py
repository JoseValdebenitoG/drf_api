
'''
Usaremos un modulo de rest_framework para poder definir las
urls desde el framework y no desde cero por nosotros
'''
from rest_framework import routers
# importamos el viewset
from .api import ProjectViewSet

# Ejecutamos el modulo y lo guardamos en una variable
router = routers.DefaultRouter()

# Registramos las rutas 
'''
Dentro del metodo register definimos la url donde se consultará.
Tambien de donde vienen los datos y
finalmente el nombre de la ruta
y este metodo creará las urls para el metodo get, post, etc
'''
router.register('api/projects', ProjectViewSet, 'projects')

# Exportamos el url patterns
urlpatterns = router.urls
