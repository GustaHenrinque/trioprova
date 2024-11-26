# Gustavo, Júlia Conconi e Rian
import csv
from collections import defaultdict
from datetime import datetime

def calcular_media_temperaturas(arquivo_csv):
    temperaturas_por_mes = defaultdict(list)
    
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        leitor_csv = csv.DictReader(file)
        
        for linha in leitor_csv:
            data = datetime.strptime(linha['Data'], '%Y-%m-%d')
            temperatura = float(linha['Temperatura'])
            
            mes_ano = (data.year, data.month)
            temperaturas_por_mes[mes_ano].append(temperatura)
    
    medias_por_mes = {
        f"{ano}-{mes:02d}": sum(temp_list) / len(temp_list)
        for (ano, mes), temp_list in temperaturas_por_mes.items()
    }
    
    return medias_por_mes


arquivo = r'C:\Users\Júlia\Documents\tarefapython-trio\trioprova\exerc.8\dados.csv'  # Use o caminho completo
media_temperaturas = calcular_media_temperaturas(arquivo)
print(media_temperaturas)