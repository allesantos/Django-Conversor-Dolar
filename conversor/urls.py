from django.urls import path  # Importa a função path, que é usada para definir rotas no Django
from . import views  # Importa o arquivo views.py do mesmo diretório para vincular as funções às URLs

# Lista de padrões de URL do aplicativo
urlpatterns = [
    path('', views.conversor_moeda, name='conversor_moeda'),  
    # Define a URL raiz ('') do aplicativo e vincula à função 'conversor_moeda' localizada em views.py
    # O parâmetro 'name' permite referenciar essa rota em templates e outras partes do código
]


