from Clientes import *

while True:
    while True:
        try:
            op=int(input("--- Menu ---\n1-Cadastro\n2-Alterar\n3-Relatório\n4-Sair\n"))
            break
        except:
            print("Valor Inválido")

    if op == 1:
        print("--- Cadstro de Cliente ---")
        nome = input("Nome: ")
        while True:
            try:
                idade = int(input("Idade: "))
                break
            except:
                print("Valor Inválido")
        while True:
            try:        
                cpf = int(input("CPF: "))
                break
            except:
                print("Valor Inválido")
        cliente1=Clientes(nome,idade,cpf)
    elif op == 2:
        print("--- Alteração de dados ---")
        nome = input("Nome: ")
        while True:
            try:
                idade = int(input("Idade: "))
                break
            except:
                print("Valor Inválido")
        while True:
            try:        
                cpf = int(input("CPF: "))
                break
            except:
                print("Valor Inválido")
        cliente1=Clientes(nome,idade,cpf)
    elif op == 3:
        Clientes.relatorio()
    else:
        print("Valor Inválido")

    
