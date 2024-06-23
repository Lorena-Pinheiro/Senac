from funcao import *

while True:
    while True:
        try:
            op=int(input('--- Menu de opções ----\n1-Clientes\n2-Peças\n3-Serviços\n4-Contas a pagar\n5-Veículos\n6-Fornecedores\n7-Sair\n'))
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
                    try:
                        id_cliente = int(input('Digite o ID do cliente: '))
                        break
                    except:
                        print("Valor Inválido.\nDigite apenas números.")
                if(id_cliente not in cliente):
                    print('Cliente não cadastrado.')
                else:
                    alterar_cliente(id_cliente)       
            elif(op2==4):
                print('--- Relatório dos Dados dos Clientes ---\n')
                relatorio_cliente(cliente)
                while True:
                    try:
                        voltar = int(input('Digite 1 para voltar.\n'))
                        if(voltar == 1):
                            break
                        else:
                            print("Valor inválido.")
                    except:
                        print('Valor Inválido.\nDigite apenas números.')
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==2):
        while True:
            while True:
                try:
                    op2=int(input('--- Peças ---\nO que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            if(op2==1): 
                cadastro_peca()
                print('Peça cadastrada.')
            elif(op2==2):
                excluir_peca()
            elif(op2==3):
                while True:
                    try:
                        id_peca = int(input('Digite o ID do peça: '))
                        break
                    except:
                        print("Valor Inválido.\nDigite apenas números.")
                if(id_peca not in peca):
                    print('Peça não cadastrada.')
                else:
                    alterar_peca(id_peca)
            elif(op2==4):
                print('--- Relatório dos Dados das Peças ---\n')
                relatorio_peca(peca)
                while True:
                    try:
                        voltar = int(input('Digite 1 para voltar.\n'))
                        if(voltar == 1):
                            break
                        else:
                            print("Valor inválido.")
                    except:
                        print('Valor Inválido.\nDigite apenas números.')
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==3):
        while True:
            while True:
                try:
                    op2=int(input('--- Serviços ---\nO que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            if(op2==1): 
                cadastro_servico()
                print('Serviço cadastrado.')
            elif(op2==2):
                excluir_servico()
            elif(op2==3):
                while True:
                    try:
                        id_servico = int(input('Digite o ID do serviço: '))
                        break
                    except:
                        print("Valor Inválido.\nDigite apenas números.")
                if(id_servico not in servico):
                    print('Serviço não cadastrado.')
                else:
                    alterar_servico(id_servico)
            elif(op2==4):
                print('--- Relatório dos Dados dos Serviços ---\n')
                relatorio_servico(servico)
                while True:
                    try:
                        voltar = int(input('Digite 1 para voltar.\n'))
                        if(voltar == 1):
                            break
                        else:
                            print("Valor inválido.")
                    except:
                        print('Valor Inválido.\nDigite apenas números.')
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==4):
        while True:
            while True:
                try:
                    op2=int(input('--- Contas a pagar ---\nO que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            if(op2==1): 
                cadastro_conta_pagar()
                print('Conta cadastrado.')
            elif(op2==2):
                excluir_conta_pagar()
            elif(op2==3):
                while True:
                    try:
                        id_conta_pagar = int(input('Digite o ID do conta: '))
                        break
                    except:
                        print("Valor Inválido.\nDigite apenas números.")
                if(id_conta_pagar not in conta_pagar):
                    print('Conta não cadastrada.')
                else:
                    alterar_conta_pagar(id_conta_pagar)
            elif(op2==4):
                print('--- Relatório dos Dados dos Contas ---\n')
                relatorio_conta_pagar(conta_pagar)
                while True:
                    try:
                        voltar = int(input('Digite 1 para voltar.\n'))
                        if(voltar == 1):
                            break
                        else:
                            print("Valor inválido.")
                    except:
                        print('Valor Inválido.\nDigite apenas números.')
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==5):
        while True:
            while True:
                try:
                    op2=int(input('--- Veículos ---\nO que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            if(op2==1): 
                cadastro_veiculo()
                print('Veículo cadastrado.')
            elif(op2==2):
                excluir_veiculo()
            elif(op2==3):
                while True:
                    try:
                        id_veiculo = int(input('Digite o ID do veículo: '))
                        break
                    except:
                        print("Valor Inválido.\nDigite apenas números.")
                if(id_veiculo not in veiculo):
                    print('Veículo não cadastrado.')
                else:
                    alterar_veiculo(id_veiculo)
            elif(op2==4):
                print('--- Relatório dos Dados dos Veículos ---\n')
                relatorio_veiculo(veiculo)
                while True:
                    try:
                        voltar = int(input('Digite 1 para voltar.\n'))
                        if(voltar == 1):
                            break
                        else:
                            print("Valor inválido.")
                    except:
                        print('Valor Inválido.\nDigite apenas números.')
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==6):
        while True:
            while True:
                try:
                    op2=int(input('--- Fornecedores ---\nO que você gostaria de fazer?\n1-Cadastrar\n2-Excluir\n3-Alterar\n4-Relatório\n5-Sair\n'))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            if(op2==1): 
                cadastro_fornecedor()
                print('Fornecedor cadastrado.')
            elif(op2==2):
                excluir_fornecedor()
            elif(op2==3):
                while True:
                    try:
                        id_fornecedor = int(input('Digite o ID do fornecedor: '))
                        break
                    except:
                        print("Valor Inválido.\nDigite apenas números.")
                if(id_fornecedor not in fornecedor):
                    print('Fornecedor não cadastrado.')
                else:
                    alterar_fornecedor(id_fornecedor)
            elif(op2==4):
                print('--- Relatório dos Dados dos Fornecedores ---\n')
                relatorio_fornecedor(fornecedor)
                while True:
                    try:
                        voltar = int(input('Digite 1 para voltar.\n'))
                        if(voltar == 1):
                            break
                        else:
                            print("Valor inválido.")
                    except:
                        print('Valor Inválido.\nDigite apenas números.')
            elif(op2==5):
                print('Saindo...')
                break
            else:
                print('Opção Inválida')
    elif(op==7):
        print('saindo...')
        break