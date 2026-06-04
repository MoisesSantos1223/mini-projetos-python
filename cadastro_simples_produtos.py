produtos = []
contador = 0

def Menu_usario():
    print("Escolha umas das opções abaixo!")
    print("1-Menu")
    print("2-Produtos")
    print("3-Sair")
    
def Produtos():
    global produtos
    global contador
    
    print("Escolha 3 produtos apenas!")
    while contador < 3:
        Produto = input("Digite um nome do produto!")
        produtos.append(Produto)
        contador += 1
        
        print(f"Produtos recolhidos : {produtos}") 
             
def sair_doProduto():
    print("Você saiu!!")
    
Menu_usario()

usario = int(input("Digite uma opção: "))

if usario == 1:
    Menu_usario()
elif usario == 2: 
    Produtos()
elif usario == 3:
        sair_doProduto()
else:
    print("Digite somente os números que estão no menu")