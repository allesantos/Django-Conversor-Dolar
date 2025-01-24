from django.shortcuts import render  # Importa a função render para renderizar templates HTML com dados contextuais
from django import forms  # Importa o módulo forms do Django para criar formulários
import requests  # Importa a biblioteca requests para fazer requisições HTTP

# Define uma classe de formulário para o conversor de moeda
class FormularioConversor(forms.Form):
    # Campo para o valor a ser convertido (float, com valor mínimo de 0)
    valor = forms.FloatField(
        label='Valor',  # Rótulo exibido para o usuário
        min_value=0,  # Impede que o valor seja negativo
        widget=forms.NumberInput(attrs={'placeholder': 'Digite o valor'})  # Adiciona um placeholder no campo de entrada
    )
    # Campo para escolher o tipo de conversão (Dólar para Real ou Real para Dólar)
    tipo_conversao = forms.ChoiceField(
        label='Converter de',  # Rótulo exibido para o usuário
        choices=(  # Define as opções disponíveis no campo de seleção
            ('usd_to_brl', 'Dólar para Real'), 
            ('brl_to_usd', 'Real para Dólar')
        )
    )

# Função para obter a cotação atual do dólar em relação ao real
def obter_cotacao():
    try:
        # Faz uma requisição GET à API para obter a cotação atual
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        response.raise_for_status()  # Levanta uma exceção se houver erro na requisição
        dados = response.json()  # Converte a resposta JSON para um dicionário Python
        return dados['rates']['BRL']  # Retorna a cotação do dólar em relação ao real
    except Exception as e:
        # Exibe um erro no console e retorna None se algo der errado
        print(f"Erro ao obter a cotação: {e}")
        return None

# Função principal para processar a conversão de moeda
def conversor_moeda(request):
    resultado_conversao = None  # Variável para armazenar o resultado da conversão
    cotacao = obter_cotacao()  # Obtém a cotação do dólar

    # Verifica se houve um erro ao obter a cotação
    if cotacao is None:
        # Renderiza uma página de erro se a cotação não foi obtida
        return render(request, 'erro.html', {'mensagem': 'Erro ao obter a cotação. Tente novamente mais tarde.'})

    # Verifica se o método da requisição é POST (formulário enviado)
    if request.method == 'POST':
        formulario = FormularioConversor(request.POST)  # Preenche o formulário com os dados enviados
        if formulario.is_valid():  # Verifica se os dados do formulário são válidos
            valor = formulario.cleaned_data['valor']  # Obtém o valor informado
            tipo_conversao = formulario.cleaned_data['tipo_conversao']  # Obtém o tipo de conversão escolhido

            # Verifica o tipo de conversão e calcula o resultado
            if tipo_conversao == 'usd_to_brl':  # Dólar para Real
                resultado_conversao = f"{valor * cotacao:,.2f} BRL".replace(',', 'X').replace('.', ',').replace('X', '.')
            elif tipo_conversao == 'brl_to_usd':  # Real para Dólar
                resultado_conversao = f"{valor / cotacao:,.2f} USD".replace(',', 'X').replace('.', ',').replace('X', '.')
    else:
        # Caso a requisição não seja POST, cria um formulário vazio
        formulario = FormularioConversor()

    # Renderiza a página do conversor de moeda com o formulário e os resultados (se houver)
    return render(request, 'conversor/conversor_moeda.html', {
        'formulario': formulario,  # O formulário a ser exibido na página
        'resultado_conversao': resultado_conversao,  # O resultado da conversão, se disponível
        'cotacao': f"{cotacao:,.2f} BRL".replace(',', 'X').replace('.', ',').replace('X', '.')  # Cotação formatada
    })
