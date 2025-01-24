from django.contrib import admin  # Importa o módulo de administração do Django
from django.urls import path, include  # Importa funções para definir rotas e incluir outras URLs

# Lista de padrões de URL da aplicação
urlpatterns = [
    path('admin/', admin.site.urls),  # Define a URL para acessar o painel de administração do Django (normalmente acessado em '/admin/')
    path('', include('conversor.urls')),  # Inclui as URLs definidas no aplicativo 'conversor' na raiz do projeto
]




