#Gustavo, Julia e Rian

import statistics
def calcular_estatisticas_nivel(niveis):
   
    media = statistics.mean(niveis)
    mediana = statistics.median(niveis)
    return media, mediana

niveis_mensais = [3.5, 4.2, 5.1, 3.8, 4.0, 4.5, 3.9, 4.1, 4.7, 5.0, 3.6, 4.3]
media, mediana = calcular_estatisticas_nivel(niveis_mensais)
print(f"Média dos níveis: {media:.2f}m")
print(f"Mediana dos níveis: {mediana:.2f}m")
