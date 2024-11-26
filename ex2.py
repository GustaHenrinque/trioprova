#Gustavo, Julia e Rian

def filtrar_eventos_por_intensidade(eventos, limite=7):
    return [evento for evento in eventos if evento['intensidade'] > limite]

eventos_catastrofes = [
    {'tipo': 'enchente', 'intensidade':10, 'local': 'Taubaté'},
    {'tipo': 'furacão', 'intensidade': 10, 'local': 'Caçapava'},
    {'tipo': 'enchente', 'intensidade': 4, 'local': 'São José dos Campos'},
    {'tipo': 'furacão', 'intensidade': 6, 'local': 'Jacareí'}
]

eventos_filtrados = filtrar_eventos_por_intensidade(eventos_catastrofes)
print(f"Eventos filtrados: {eventos_filtrados}")
