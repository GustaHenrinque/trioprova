def cadastra_produto(nome, preco, quantidade):
    """
    Cadastra um produto e retorna um dicionário com seus dados.
    """
    return {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

produtos = []

for i in range(1, 6):
    print(f"Cadastro do Produto {i}:")
    nome = input("  Nome do produto: ")
    preco = float(input("  Preço: R$ "))
    quantidade = int(input("  Quantidade: "))
    produto = cadastra_produto(nome, preco, quantidade)
    produtos.append(produto)

print("\nProdutos cadastrados:")
for i, produto in enumerate(produtos, start=1):
    print(f"Produto {i}: Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
