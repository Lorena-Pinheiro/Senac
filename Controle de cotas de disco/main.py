from Usuarios import*

while True:
    while True:
        try:
            op = int(input("---- Menu ----\n1- Cadastra usuário\n2-Gerar relatório\n"))
            break
        except:
            print("Valor Inválido. Digite apenas números.")
            
    if op == 1:
        usuario = Usuario()
        usuario.cadastro_usuario()