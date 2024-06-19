from funcao import(cadastro_cliente,excluir_cliente)

while True:
    op=int(input('Menu de opções:\n1-Clientes\n2-Peças\n3-Serviços\n4-Contas a pagar\n5-Veículos\n6-Fornecedor\n7-Sair\n'))
    if(op==1):
        while True:
            op2=int(input('O que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
            if(op2==1):
                cadastro_cliente()
                while True:                
                    op3=int(input('1-Enviar         2-Editar\n1'))
                    if(op3==1):
                        print('enviando...')
                        break
                    elif(op3==2):
                        break
                    else:
                        print('Opção Inválida')
                        break
            elif(op2==2):
                excluir_cliente()
            elif(op==3):
                alterar_cliente()
            elif(op2==4):
                relatorio_cliente()
            elif(op2==5):
                print('saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==7):
        print('saindo...')
        break
    else:
        print('Opção Inválida')