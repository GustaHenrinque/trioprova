def calcula_media_temperatura(temperaturas):
    """
    Calcula a média das temperaturas fornecidas em uma lista.
    """
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)
cidades_temperaturas = []

for i in range(1, 6):
    print(f"Cidade {i}:")
    temperaturas = []
    for j in range(3): 
        temp = float(input(f"  Insira a temperatura {j + 1}: "))
        temperaturas.append(temp)
    cidades_temperaturas.append(temperaturas)

print("\nMédias de temperatura por cidade:")
for i, temps in enumerate(cidades_temperaturas, start=1):
    media = calcula_media_temperatura(temps)
    print(f"Cidade {i}: {media:.2f}°C")
