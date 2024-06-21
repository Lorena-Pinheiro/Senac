#Dicionarios
cliente={} #4/4
peca={} #4/4
servico={}
conta_pagar={} #1/4
veiculo={}
fornecedor={}


#Funções do Cliente
def cadastro_cliente():
    print('---Informe as informações do cliente---')
    while True:
        try:
            id_cliente=int(input('ID: '))
            break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    nome=input('Nome: ')
    while True:
        try:
            cpf=int(input('CPF: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    data_nascimento=input('Data de nascimento: ')
    bairro=input('Bairro: ')
    rua=input('Rua: ')
    while True:
        try:
            numero_contato=int(input('Número para contato: '))
            break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    email=input('Email: ')
    cliente[id_cliente]={'ID':id_cliente,
                         'Nome':nome,
                         'CPF':cpf,
                         'Data de nascimento':data_nascimento,
                         'Bairro':bairro,
                         'Rua':rua,
                         'Número de contato':numero_contato,
                         'Email':email}


def excluir_cliente():
    while True:
        id_cliente=int(input('Digite o ID do cliente: '))
        if(type(id_cliente) is not int):
            print('Valor Inválido.\nDigite apenas números.')
        else:
            break
    if(id_cliente in cliente):
        del cliente[id_cliente]
        print('Cliente excluido.')
    else:
        print('Não existe um cliente com esse ID.')


def alterar_cliente():
    while True:
        print('--- Alteração das Informações do Cliente ----')
        while True:
            id_cliente=int(input('Digite o ID do cliente: '))
            if(type(id_cliente) is not int):
                print("Valor Inválido.\nDigite apenas números.")
            elif(id_cliente not in cliente):
                print('Cliente não cadastrado.')
            else:
                break
        while True:
            categoria=input('Escolha a categoria que será alterada:\n1-Nome\n2-CPF\n3-Data de nascimento\n4-Bairo\n5-Rua\n6-Número para contato\n7-Email')
            if(type(categoria) is not int):
                print("Valor Inválido.\nDigite apenas números.")  
            else:
                break 
        if(categoria==1):
            novo_valor = input('Novo Nome: ')
            cliente[id_cliente]['Nome'] = novo_valor
        elif(categoria==2):
            while True:
                novo_valor=int(input('Novo CPF: '))
                if(novo_valor in cliente):
                    print('CPF já cadastrado.\nDigite outro.')
                elif(type(novo_valor) is not int):
                    print("Valor Inválido.\nDigite apenas números.")
                else:
                    break
            cliente[id_cliente]['CPF'] = novo_valor
        elif(categoria==3):
            novo_valor = input('Nova data de nascimento: ')
            cliente[id_cliente]['Data de nascimento'] = novo_valor
        elif(categoria==4):
            novo_valor = input('Novo bairro: ')
            cliente[id_cliente]['Bairro'] = novo_valor
        elif(categoria==5):
            novo_valor = input('Nova rua: ')
            cliente[id_cliente]['Rua'] = novo_valor
        elif(categoria==6):
            novo_valor = int(input('Nova número para contato: '))
            cliente[id_cliente]['Número para contato'] = novo_valor
        elif(categoria==7):
            novo_valor = input('Novo email: ')
            cliente[id_cliente]['Email'] = novo_valor
        while True:
            op=int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não'))
            if(type(op) is not int):
                print("Valor Inválido.\nDigite apenas números.")
            elif(op != 1 or op != 2):
                print('Opção não existente.')
            else:
                break
        if(op==2):
            print('Valor alterado e salvo.')
            break
        elif(op==1):
            print('Voltando...')           

    
def relatorio_cliente():
    print(cliente)
    



#Funções da Peça
def cadastro_peca():
    while True:
        id_peca=int(input('ID:'))
        if(type(id_peca) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    while True:
        numero_peca=int(input('Número: '))
        if (numero_peca in peca):
            print('Número já cadastrado.\nDigite outro.')
        elif(type(numero_peca) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    nome=input('Nome:')
    marca=input('Marca: ')
    data_fabricacao=input('Data de fabricação: ')
    funcao=input('Função: ')
    while True:
        peso=input('Peso: ')
        if(type(peso) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    material=input('Material: ')
    while True:
        preco=input('Preço: ')
        if(type(preco) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    while True:
        quantidade=input('Quantidade em estoque: ')
        if(type(quantidade) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    localizacao=input('Localização no veículo: ')
    peca[numero_peca]={'ID':id_peca,
                       'Nome':nome,
                       'Marca':marca,
                       'Data de fabricacao':data_fabricacao,
                       'Função':funcao,
                       'Peso':peso,
                       'Material':material,
                       'Preço':preco,
                       'Quantidade':quantidade,
                       'Localização':localizacao}


def excluir_peca():
    while True:
        id_peca=int(input('Digite o número da peça: '))
        if(type(id_peca) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    if(id_peca in cliente):
        del peca[id_peca]
        print('Peça excluido.')
    else:
        print('Não existe uma peça com esse número.')


def alterar_peca():
    while True:
        print('--- Alteração das Informações da Peça ----')
        while True:
            id_peca=int(input('Digite o ID da peça: '))
            if(type(id_peca) is not int):
                print("Valor Inválido.\nDigite apenas números.")
            elif(id_peca not in cliente):
                print('Peça não cadastrado.')
            else:
                break
        while True:
            categoria=input('Escolha a categoria que será alterada:\n1-Nome\n2-Marca\n3-Data de fabricação\n4-Função\n5-Peso\n6-Material\n7-Preço\n8-Quantidade\n9-Localização')
            if(type(categoria) is not int):
                print("Valor Inválido.\nDigite apenas números.")  
            else:
                break      
        if(categoria==1):
            novo_valor = input('Novo Nome: ')
            peca[id_peca]['Nome'] = novo_valor
        elif(categoria==2):
            novo_valor=input('Nova marca: ')
            peca[id_peca]['Marca'] = novo_valor
        elif(categoria==3):
            novo_valor = input('Nova data de fabricação: ')
            peca[id_peca]['Data de fabricacao'] = novo_valor
        elif(categoria==4):
            novo_valor = input('Novo Função: ')
            peca[id_peca]['funcao'] = novo_valor
        elif(categoria==5):
            while True:
                novo_valor = int(input('Novo peso: '))
                if(type(novo_valor) is not int):
                    print('Valor Inválido.\nDigite apenas números.')
                else:
                    break
            peca[id_peca]['Peso'] = novo_valor
        elif(categoria==6):
            novo_valor = input('Novo material')
            peca[id_peca]['Material'] = novo_valor
        elif(categoria==7):
            while True:
                novo_valor = input('Novo preço: ')
                if(type(novo_valor) is not int):
                    print('Valor Inválido.\nDigite apenas números.')
                else:
                    break
            peca[id_peca]['preco'] = novo_valor
        elif(categoria==8):
            while True:
                novo_valor=int(input('Nova quantidade: '))
                if(type(novo_valor) is not int):
                    print('Valor Inválido.\nDigite apenas números.')
                else:
                    break
            peca[id_peca]['Quantidade'] = novo_valor
        elif(categoria==9):
            novo_valor=input('Nova localização: ')
            peca[id_peca]['Localização'] = novo_valor
        while True:
            op=int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não'))
            if(type(op) is not int):
                print("Valor Inválido.\nDigite apenas números.")
            elif(op != 1 or op != 2):
                print('Opção não existente.')
            else:
                break
        if(op==2):
            print('Valor alterado e salvo.')
            break
        elif(op==1):
            print('Voltando...')


def relatorio_peca():
    print(cliente)





#Funções do Serviço
def cadastro_servico():
    print('---Informe as informações do Serviço---')
    while True:
        id_servico=int(input('ID: '))
        if(type(id_servico) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    tipo=input('Tipo do serviço: ')
    while True:
        custo_maoDeobra=int(input("Custo da mão de obra: "))
        if(type(custo_maoDeobra) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    peca_usada=input('Peças usadas: ')
    while True:
        custo_peca=int(input('Custo das peças: '))
        if(type(custo_peca) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    while True:
        valor_total=int(input('Valor total do serviço: '))
        if(type(valor_total) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    tempo=input('Tempo estimado de realização: ')
    tarefa_realizada=input('Tarefas realizadas: ')
    ferramentas_usadas=input('Ferramentas usadas: ')
    servico[id_servico]={}
 
    
def excluir_servico():
    while True:
        id_servico=int(input('Digite o número da peça: '))
        if(type(id_servico) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    if(id_servico in servico):
        del servico[id_servico]
        print('Serviço excluido.')
    else:
        print('Não existe um serviço com esse ID.')


def alterar_servico():
    while True:
        print('--- Alteração das Informações do Serviço ----')
        while True:
            id_servico=int(input('Digite o ID da peça: '))
            if(type(id_servico) is not int):
                print("Valor Inválido.\nDigite apenas números.")
            elif(id_servico not in cliente):
                print('Serviço não cadastrado.')
            else:
                break
        while True:
            categoria=input('Escolha a categoria que será alterada:\n1-Nome\n2-Marca\n3-Data de fabricação\n4-Função\n5-Peso\n6-Material\n7-Preço\n8-Quantidade\n9-Localização')
            if(type(categoria) is not int):
                print("Valor Inválido.\nDigite apenas números.")  
            else:
                break      
        if(categoria==1):
            novo_valor = input('Novo Nome: ')
            servico[id_servico]['Nome'] = novo_valor
        elif(categoria==2):
            novo_valor=input('Nova marca: ')
            servico[id_servico]['Marca'] = novo_valor
        elif(categoria==3):
            novo_valor = input('Nova data de fabricação: ')
            servico[id_servico]['Data de fabricacao'] = novo_valor
        elif(categoria==4):
            novo_valor = input('Novo Função: ')
            servico[id_servico]['funcao'] = novo_valor
        elif(categoria==5):
            while True:
                novo_valor = int(input('Novo peso: '))
                if(type(novo_valor) is not int):
                    print('Valor Inválido.\nDigite apenas números.')
                else:
                    break
            servico[id_servico]['Peso'] = novo_valor
        elif(categoria==6):
            novo_valor = input('Novo material')
            servico[id_servico]['Material'] = novo_valor
        elif(categoria==7):
            while True:
                novo_valor = input('Novo preço: ')
                if(type(novo_valor) is not int):
                    print('Valor Inválido.\nDigite apenas números.')
                else:
                    break
            servico[id_servico]['preco'] = novo_valor
        elif(categoria==8):
            while True:
                novo_valor=int(input('Nova quantidade: '))
                if(type(novo_valor) is not int):
                    print('Valor Inválido.\nDigite apenas números.')
                else:
                    break
            servico[id_servico]['Quantidade'] = novo_valor
        elif(categoria==9):
            novo_valor=input('Nova localização: ')
            servico[id_servico]['Localização'] = novo_valor
        while True:
            op=int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não'))
            if(type(op) is not int):
                print("Valor Inválido.\nDigite apenas números.")
            elif(op != 1 or op != 2):
                print('Opção não existente.')
            else:
                break
        if(op==2):
            print('Valor alterado e salvo.')
            break
        elif(op==1):
            print('Voltando...')


def relatorio_servico():
    print(servico)





#Funções das contas a pagar
def cadastro_contas_pagar():
    while True:
        id_contas_pagar=int(input('ID: '))
        if(type(numero_conta) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    while True:
        numero_conta=int(input('Número da conta: '))
        if(type(numero_conta) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    data_emissao=input('Data da emissão: ')
    data_vencimento=input('Data do vencimento:')
    while True:
        valor=int(input('Valor a ser pago: '))
        if(type(valor) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    nome_empresa=input('Nome da empresa ou entidade que emitiu a conta: ')
    endereco_empresa=input('Endereço da empresa:')
    while True:
        numero_contato=int(input('Telefone de contato: '))
        if(type(numero_contato) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    email=input('Email de contato: ')
    while True:
        cnpj=int(input('CNPJ: '))
        if(type(cnpj) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    nome_responsavel=input('Nome do responsável pelo pagamento: ')
    endereco_responsavel=input('Endereço do responsável: ')
    while True:
        cpf=input('CPF do responsável: ')
        if(type(cpf) is not int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break