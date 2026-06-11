"""
Em uma loja, o funcionário precisa registrar o preço de vários produtos comprados por um cliente. O sistema
deve continuar recebendo preços até que seja digitado o valor 0, indicando o fim da compra. Ao final, o
programa deve apresentar o valor total da compra, a quantidade de produtos registrados, o produto mais caro,
o produto mais barato e quantos produtos custaram mais de R$50. O valor 0 deve ser usado apenas para
encerrar o programa e não deve ser considerado nos cálculos.
"""

def cadastrar_produtos():
    
    lista = []
    soma = 0
    contador_50 = 0

    while True:
        
        preco = float(input("Digite o preço do produto: R$ "))

        if preco == 0:
            break

        lista.append(preco)
        soma += preco

        if preco > 50:
            contador_50 += 1

    return lista, soma, contador_50


def mostrar_resumo(lista, soma, contador_50):
    
    if len(lista) == 0:
        print("Nenhum produto foi cadastrado.")
        return

    quantidade = len(lista)
    maior_preco = max(lista)
    menor_preco = min(lista)

    print("\n===== RESUMO DA COMPRA =====")
    print(f"Produtos cadastrados: {lista}")
    print(f"Total da compra: R$ {soma:.2f}")
    print(f"Quantidade de produtos: {quantidade}")
    print(f"Produto mais caro: R$ {maior_preco:.2f}")
    print(f"Produto mais barato: R$ {menor_preco:.2f}")
    print(f"Produtos acima de R$50,00: {contador_50}")


def sistema():
    lista, soma, contador_50 = cadastrar_produtos()
    mostrar_resumo(lista, soma, contador_50)


sistema()