# Conversor de Moeda (Dólar <-> Real)
 
## Índice
- [Descrição](#Descrição)
- [Recursos](#Recursos)
- [Tecnologias Utilizadas](#Tecnologias)
- [Pré-requisitos](#Pré-requisitos)
- [Uso](#Uso)
- [Instalação](#Instalação)
- [Contribuição](#Contribuição)
- [Licença](#Licença)

## Descrição
Este projeto é um aplicativo Django que permite aos usuários converter valores entre dólares americanos (USD) e reais brasileiros (BRL). Ele utiliza a cotação atualizada do dólar, obtida em tempo real por meio de uma API, para realizar as conversões com precisão.

## Recursos
- Conversão de dólar para real (USD -> BRL).
- Conversão de real para dólar (BRL -> USD).
- Atualização automática da cotação do dólar em tempo real usando uma API externa.
- Interface intuitiva para inserção do valor e seleção do tipo de conversão.

## Tecnologias
- __Backend:__ Python 3.x, Django 5.x e API de Conversão (ExchangeRate API)
- __Frontend:__ HTML5, CSS3 (com integração ao Google Fonts)

## Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas em sua máquina antes de iniciar:
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado para isolamento do ambiente)
- Git

## Uso
Digite o valor que deseja converter.

1. Escolha o tipo de conversão (dólar para real ou real para dólar).
2. Clique no botão "Converter" para visualizar o resultado com base na cotação atual.
   
## Instalação
1. Clone o repositório para sua máquina local:

    ```
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie e ative um ambiente virtual:

    ```
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:

    ```
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```
    python manage.py runserver
    ```

6. Acesse o sistema em http://127.0.0.1:8000/ no seu navegador.

## Contribuição
Sinta-se à vontade para contribuir com este projeto. Siga estas etapas:

1. Faça um fork do repositório.

2. Crie uma nova branch para sua feature/bugfix:

    ```
    git checkout -b minha-feature
    ```

3. Envie suas alterações:

    ```
    git push origin minha-feature
    ```

4. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.

