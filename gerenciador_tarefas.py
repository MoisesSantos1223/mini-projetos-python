lista = []

print("=====Gerenciador de tarefas======")

def menu_Tarefas():
    print()
    print("Escolha uma das opções abaixo")
    print()
    print("1- Adicionar Tarafa")
    print("2- Mostrar tarefas")
    print("3- Remover tarefas")
    print("4- Sair")
    print()
    
def adicionar_tarefas():
    global lista
    contador = 0
    
    print("Digite apenas 5 tarefas")
    print()
    
    while contador < 5:
        tarefa = input("Escreva uma tarefa: ")
        
        contador += 1
        lista.append(tarefa)
    print()    
    print("Tarefa adicionada com sucesso!")
    
def mostra_tarefas():
    print(lista)

def Remover_tarefas():
    print("Escolha umas das tarefas para remover")
    print()
    print(lista)
    print()
    RemoverTarefa = input("Digite a tarefa que desaja remover: ")
    print()
    
    if RemoverTarefa in lista:
        lista.remove(RemoverTarefa)
        print("Tarefa removida com sucesso!", lista)
    else:
        print("Error, tente novamente mais tarde")
        
def sair():
    print("Saindo do gerenciador de tarefas.........")
    
while True:
    menu_Tarefas()
    
    usario = int(input("Digite o número de uma opção: "))
    print()
    
    if usario == 1:
        adicionar_tarefas()
    elif usario == 2:
        mostra_tarefas()
    elif usario == 3:
        Remover_tarefas()
    elif usario == 4:
        sair()
        break
    else:
        print("Digite apenas umas das opções!")