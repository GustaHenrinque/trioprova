# Gustavo, Júlia Conconi e Rian
import csv
def classificar_desastres(desastres):
    classificacoes = []
    
    for desastre in desastres:
        nome = desastre["Tipo"]
        intensidade = float(desastre["Intensidade"])
        
        if intensidade < 3:
            impacto = "Baixo impacto"
        elif 3 <= intensidade <= 6:
            impacto = "Médio impacto"
        else:
            impacto = "Alto impacto"
        
        classificacoes.append({
            "Tipo": nome,
            "Intensidade": intensidade,
            "Impacto": impacto
        })
    
    return classificacoes

def exibir_resultados(classificacoes):
    print("\nClassificação de Desastres:")
    print("-" * 30)
    for c in classificacoes:
        print(f"Desastre: {c['Tipo']}, Intensidade: {c['Intensidade']}, Impacto: {c['Impacto']}")
    print("-" * 30)

def salvar_resultados_csv(classificacoes, arquivo_saida):
    with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Tipo", "Intensidade", "Impacto"])
        writer.writeheader()
        writer.writerows(classificacoes)
    print(f"Resultados salvos em: {arquivo_saida}")

def carregar_dados_csv(arquivo_entrada):
    try:
        with open(arquivo_entrada, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [linha for linha in reader]
    except FileNotFoundError:
        print("Arquivo de entrada não encontrado!")
        return []

# Programa principal
if __name__ == "__main__":
    print("Sistema de Classificação de Desastres Naturais")
    print("-" * 50)
    print("1. Carregar dados de um arquivo CSV")
    print("2. Inserir dados manualmente")
    opcao = input("Escolha uma opção (1 ou 2): ")

    desastres = []

    if opcao == "1":
        arquivo_entrada = input("Digite o caminho do arquivo CSV de entrada: ")
        desastres = carregar_dados_csv(arquivo_entrada)
    elif opcao == "2":
        print("\nDigite as informações dos desastres:")
        while True:
            tipo = input("Tipo de desastre (ex: Tremor de terra): ")
            intensidade = input("Intensidade (valor numérico): ")
            desastres.append({"Tipo": tipo, "Intensidade": intensidade})
            
            continuar = input("Adicionar outro? (s/n): ").lower()
            if continuar != 's':
                break
    else:
        print("Opção inválida! Encerrando o programa.")
        exit()

    if desastres:
        classificacoes = classificar_desastres(desastres)
        exibir_resultados(classificacoes)
        
        salvar = input("Deseja salvar os resultados em um arquivo CSV? (s/n): ").lower()
        if salvar == "s":
            arquivo_saida = input("Digite o caminho do arquivo de saída: ")
            salvar_resultados_csv(classificacoes, arquivo_saida)
    else:
        print("Nenhum dado foi processado.")
