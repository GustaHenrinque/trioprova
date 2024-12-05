# Gustavo, Júlia Conconi e Rian
import matplotlib.pyplot as plt

def gerar_grafico_temperaturas(dados):

    datas = [item["data"] for item in dados]
    temperaturas_max = [item["temp_max"] for item in dados]
    temperaturas_min = [item["temp_min"] for item in dados]

   
    plt.figure(figsize=(10, 6))
    x_pos = range(len(datas)) 

    plt.bar(x_pos, temperaturas_max, color="tomato", width=0.4, label="Temp. Máxima")
    plt.bar([x + 0.4 for x in x_pos], temperaturas_min, color="skyblue", width=0.4, label="Temp. Mínima")

    plt.xticks([x + 0.2 for x in x_pos], datas, rotation=45)
    plt.xlabel("Data")
    plt.ylabel("Temperatura (°C)")
    plt.title("Temperaturas Máximas e Mínimas - Últimos 7 Dias")
    plt.legend()

    plt.tight_layout()
    plt.show()

dados_climaticos = [
    {"data": "2024-11-20", "temp_max": 30, "temp_min": 20},
    {"data": "2024-11-21", "temp_max": 32, "temp_min": 22},
    {"data": "2024-11-22", "temp_max": 29, "temp_min": 19},
    {"data": "2024-11-23", "temp_max": 28, "temp_min": 18},
    {"data": "2024-11-24", "temp_max": 27, "temp_min": 17},
    {"data": "2024-11-25", "temp_max": 31, "temp_min": 21},
    {"data": "2024-11-26", "temp_max": 33, "temp_min": 23},
]

gerar_grafico_temperaturas(dados_climaticos)

