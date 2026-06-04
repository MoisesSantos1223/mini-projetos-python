usario_correto = "moises"
senha_correta = "1234"
tentativa = 3

while tentativa > 0:
    usario = input("Digite o seu Usuario: ")
    senha = input("Digite a sua senha: ")
    
    if usario == usario_correto and senha == senha_correta:
        print("Acesso liberado")
        break
    else:
        print("Usuario ou senha está incorreto!!!")
        tentativa = tentativa - 1
        
        if tentativa == 0:
            print("Acesso Bloqueado")