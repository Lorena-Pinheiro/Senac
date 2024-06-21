from funcao import(cadastro_cliente,excluir_cliente,alterar_cliente,relatorio_cliente,cadastro_peca,excluir_peca,alterar_peca,relatorio_peca,cadastro_servico,excluir_servico,alterar_servico,relatorio_servico)

while True:
    op=int(input('--- Menu de opções ----\n1-Clientes\n2-Peças\n3-Serviços\n4-Contas a pagar\n5-Veículos\n6-Fornecedor\n7-Sair\n'))
    if(op==1):
        while True:
            op2=int(input('--- Clientes ---\nO que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
            if(op2==1):
                while True: 
                    cadastro_cliente()               
                    op3=int(input('1-Enviar         2-Editar\n'))
                    if(op3==1):
                        print('Enviando...')
                        break
                    elif(op3==2):
                        print('')
                    elif(type(op3) is not int):
                        print('Opção Inválida.\nDigite apenas números.')
                        break
                print('Cliente cadastrado.')
            elif(op2==2):
                excluir_cliente()
            elif(op==3):
                alterar_cliente()
            elif(op2==4):
                relatorio_cliente()
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==2):
        while True:
            op2=int(input('--- Peças ---\nO que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
            if(op2==1):
                while True: 
                    cadastro_peca()               
                    op3=int(input('1-Enviar         2-Editar\n'))
                    if(op3==1):
                        print('Enviando...')
                        break
                    elif(op3==2):
                        print('')
                    elif(type(op3) is not int):
                        print('Opção Inválida.\nDigite apenas números.')
                        break
                print('Peça cadastrado.')
            elif(op2==2):
                excluir_peca()
            elif(op==3):
                alterar_peca()
            elif(op2==4):
                relatorio_peca()
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==3):
        while True:
            op2=int(input('--- Serviços ---\nO que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
            if(op2==1):
                while True: 
                    cadastro_servico()               
                    op3=int(input('1-Enviar         2-Editar\n'))
                    if(op3==1):
                        print('Enviando...')
                        break
                    elif(op3==2):
                        print('')
                    elif(type(op3) is not int):
                        print('Opção Inválida.\nDigite apenas números.')
                        break
                print('servico cadastrado.')
            elif(op2==2):
                excluir_servico()
            elif(op==3):
                alterar_servico()
            elif(op2==4):
                relatorio_servico()
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==7):
        print('saindo...')
        break
    else:
        print('Opção Inválida.\nDigite apenas números.')