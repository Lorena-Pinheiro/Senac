from funcao import *

while True:
    while True:
        try:
            op=int(input('--- Menu de opções ----\n1-Clientes\n2-Peças\n3-Serviços\n4-Contas a pagar\n5-Veículos\n6-Fornecedor\n7-Sair\n'))
            break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    if(op==1):
        while True:
            while True:
                try:
                    op2=int(input('--- Clientes ---\nO que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            if(op2==1): 
                cadastro_cliente()
                print('Cliente cadastrado.')
            elif(op2==2):
                excluir_cliente()
            elif(op2==3):
                while True:
                    alterar_cliente()
                    while True:
                        try:
                            op3=int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não\n'))
                            break
                        except:
                            print("Valor Inválido.\nDigite apenas números.")
                    if(op3 != 1 or op3 != 2):
                        print('Opção Inválida.')
                    elif(op3==2):
                        print('Valor alterado e salvo.')
                        break
                    elif(op3==1):
                        break
            elif(op2==4):
                relatorio_cliente()
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    
    
    elif(op==7):
        print('saindo...')
        break