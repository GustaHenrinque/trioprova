#Gustavo, Julia Conconi e Rian

def cidade_com_maior_temperatura(dados_climaticos):

    cidade_mais_quente = max(dados_climaticos, key=lambda cidade: dados_climaticos[cidade]['temperatura'])
    return cidade_mais_quente

dados = {
    'Caçapava': {'temperatura': 33, 'umidade': 40, 'vento': 7},
    'Taubaté': {'temperatura': 29, 'umidade': 55, 'vento': 11},
    'São José dos Campos': {'temperatura': 28, 'umidade': 40, 'vento': 8}
}

print(f"A cidade com maior temperatura é: {cidade_com_maior_temperatura(dados)}")
