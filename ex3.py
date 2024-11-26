#Gustavo, Julia e Rian

def calcular_poupanca(valor_diario):
    poupanca_anual = valor_diario * 365
    return poupanca_anual

valor = float(input("Digite quanto você quer poupar por dia: R$ "))
poupanca = calcular_poupanca(valor)
print(f"Você pouparia R$ {poupanca:.2f} em 1 ano!")
