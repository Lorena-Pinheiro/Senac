#Dicionarios
cliente={} #4/4
peca={} #4/4
servico={} #4/4
conta_pagar={} #4/4
veiculo={} #4/4
fornecedor={} #4/4


#Funções do Cliente
def cadastro_cliente():
    print('---Digite as informações do cliente---')
    while True:
        try:
            id_cliente=int(input('ID: '))
            if id_cliente in cliente:
                print('ID já cadastrado. Por favor, escolha outro ID.')
            else:
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
        try:
            id_cliente=int(input('Digite o ID do cliente: '))
            break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    if(id_cliente in cliente):
        del cliente[id_cliente]
        print('Cliente excluido.')
    else:
        print('Não existe um cliente com esse ID.')


def alterar_cliente(id_cliente):
    print('--- Alteração dos Dados do Cliente ----')
    while True:
        while True:
            try:
                categoria = int(input('Escolha a categoria que será alterada:\n1-Nome\n2-CPF\n3-Data de nascimento\n4-Bairro\n5-Rua\n6-Número para contato\n7-Email\n8-sair\n'))
                break
            except:
                print("Valor Inválido.\nDigite apenas números.")   
        if(categoria == 1):
            novo_valor = input('Novo Nome: ')
            cliente[id_cliente]['Nome'] = novo_valor
        elif(categoria == 2):
            while True:
                try:
                    novo_valor = int(input('Novo CPF: '))
                    break
                except:
                    print("Valor Inválido.\nDigite apenas números.")
            cliente[id_cliente]['CPF'] = novo_valor
        elif(categoria == 3):
            novo_valor = input('Nova data de nascimento: ')
            cliente[id_cliente]['Data de nascimento'] = novo_valor
        elif(categoria == 4):
            novo_valor = input('Novo bairro: ')
            cliente[id_cliente]['Bairro'] = novo_valor
        elif(categoria == 5):
            novo_valor = input('Nova rua: ')
            cliente[id_cliente]['Rua'] = novo_valor
        elif(categoria == 6):
            while True:
                try:
                    novo_valor = int(input('Novo número para contato: '))
                    break
                except:
                    print("Valor Inválido.\nDigite apenas números.")
            cliente[id_cliente]['Número para contato'] = novo_valor
        elif(categoria == 7):
            novo_valor = input('Novo email: ')
            cliente[id_cliente]['Email'] = novo_valor
        elif(categoria == 8):
            break
        else:
            print('Opção Inválida')
            continue
        while True:
            try:
                op = int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não\n'))
                if(op == 1 or op == 2):
                    break
                else:
                    print('Opção Inválida.')
            except:
                print("Valor Inválido.\nDigite apenas números.")
        if(op == 2):
            print('Valor alterado e salvo.')
            break
        elif(op == 1):
            print('Voltando...')          

    
def relatorio_cliente(cliente):
    tamanho=len(cliente)
    if(tamanho==0):
        print('Nenhum cliente cadastrado.')
    else:
        for chave, valor in cliente.items():
            if isinstance(valor, dict):
                print(f'\n{chave}')
                relatorio_cliente(valor)
            else:
                print(f'{chave}: {valor}')

    



#Funções da Peça
def cadastro_peca():
    print('---Digite as informações da Peça---')
    while True:
        try:
            id_peca=int(input('ID:'))
            if id_peca in peca:
                print('ID já cadastrado. Por favor, escolha outro ID.')
            else:
                break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    while True:
        try:
            numero_peca=int(input('Número: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
        if (numero_peca in peca):
            print('Número já cadastrado.\nDigite outro.')
        else:
            break
    nome=input('Nome:')
    marca=input('Marca: ')
    data_fabricacao=input('Data de fabricação: ')
    funcao=input('Função: ')
    while True:
        try:
            peso=int(input('Peso: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    material=input('Material: ')
    while True:
        try:
            preco=int(input('Preço: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    while True:
        try:
            quantidade=int(input('Quantidade em estoque: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
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
        try:
            id_peca=int(input('Digite o ID da peça: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    if(id_peca in peca):
        del peca[id_peca]
        print('Peça excluida.')
    else:
        print('Não existe uma peça com esse ID.')


def alterar_peca(id_peca):
    print('--- Alteração dos Dados da Peça ----')
    while True:
        while True:
            try:
                categoria = int(input('Escolha a categoria que será alterada:\n1-Nome\n2-CPF\n3-Data de nascimento\n4-Bairro\n5-Rua\n6-Número para contato\n7-Email\n8-sair\n'))
                break
            except:
                print("Valor Inválido.\nDigite apenas números.")
        if(categoria == 1):
            novo_valor = input('Novo Nome: ')
            peca[id_peca]['Nome'] = novo_valor
        elif(categoria == 2):
            novo_valor = input('Nova marca: ')
            peca[id_peca]['Marca'] = novo_valor
        elif(categoria == 3):
            novo_valor = input('Nova data de fabricação: ')
            peca[id_peca]['Data de fabricacao'] = novo_valor
        elif(categoria == 4):
            novo_valor = input('Nova função: ')
            peca[id_peca]['funcao'] = novo_valor
        elif(categoria == 5):
            while True:
                try:
                    novo_valor = int(input('Novo peso: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            peca[id_peca]['Peso'] = novo_valor
        elif(categoria == 6):
            novo_valor = input('Novo material: ')
            peca[id_peca]['Material'] = novo_valor
        elif(categoria == 7):
            while True:
                try:
                    novo_valor = int(input('Novo preço: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            peca[id_peca]['preco'] = novo_valor
        elif(categoria == 8):
            while True:
                try:
                    novo_valor = int(input('Nova quantidade: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            peca[id_peca]['Quantidade'] = novo_valor
        elif(categoria == 9):
            novo_valor = input('Nova localização: ')
            peca[id_peca]['Localização'] = novo_valor
        elif(categoria == 10):
            print('Saindo da alteração.')
            break
        else:
            print('Opção Inválida')
            continue
        while True:
            try:
                op = int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não\n'))
                if(op == 1 or op == 2):
                    break
                else:
                    print('Opção Inválida.')
            except:
                print("Valor Inválido.\nDigite apenas números.")
        if(op == 2):
            print('Valor alterado e salvo.')
            break
        elif(op == 1):
            print('Voltando...')


def relatorio_peca(peca):
    tamanho=len(peca)
    if(tamanho==0):
        print('Nenhum peça cadastrada.')
    else:
        for chave, valor in peca.items():
            if isinstance(valor, dict):
                print(f'\n{chave}')
                relatorio_peca(valor)
            else:
                print(f'{chave}: {valor}')





#Funções do Serviço
def cadastro_servico():
    print('---Digite as informações do Serviço---')
    while True:
        try:
            id_servico=int(input('ID: '))
            if id_servico in servico:
                print('ID já cadastrado. Por favor, escolha outro ID.')
            else:
                break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    tipo=input('Tipo do serviço: ')
    while True:
        try:
            custo_maoDeobra=int(input("Custo da mão de obra: "))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    peca_usada=input('Peças usadas: ')
    while True:
        try:
            custo_peca=int(input('Custo das peças: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    while True:
        try:
            valor_total=int(input('Valor total do serviço: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    tempo=input('Tempo estimado de realização: ')
    tarefa_realizada=input('Tarefas realizadas: ')
    ferramentas_usadas=input('Ferramentas usadas: ')
    servico[id_servico]={'Id':id_servico,
                         'Tipo':tipo,
                         'Custo da Mão de Obra':custo_maoDeobra,
                         'Peça Usada':peca_usada,
                         'Custo da Peça':custo_peca,
                         'Valor Total':valor_total,
                         'Tempo':tempo,
                         'Tarefa realizada':tarefa_realizada,
                         'Ferramentas Usadas':ferramentas_usadas}
 
    
def excluir_servico():
    while True:
        try:
            id_servico=int(input('Digite o número da peça: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    if(id_servico in servico):
        del servico[id_servico]
        print('Serviço excluido.')
    else:
        print('Não existe um serviço com esse ID.')


def alterar_servico(id_servico):
    print('--- Alteração da Dados do Serviço ---')
    while True:
        while True:
            try:
                categoria = int(input('Escolha a categoria que será alterada:\n1-Nome\n2-CPF\n3-Data de nascimento\n4-Bairro\n5-Rua\n6-Número para contato\n7-Email\n8-sair\n'))
                break
            except:
                print("Valor Inválido.\nDigite apenas números.")        
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
                try:
                    novo_valor = int(input('Novo peso: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            servico[id_servico]['Peso'] = novo_valor
        elif(categoria==6):
            novo_valor = input('Novo material')
            servico[id_servico]['Material'] = novo_valor
        elif(categoria==7):
            while True:
                try:
                    novo_valor = int(input('Novo preço: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            servico[id_servico]['preco'] = novo_valor
        elif(categoria==8):
            while True:
                try:
                    novo_valor=int(input('Nova quantidade: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            servico[id_servico]['Quantidade'] = novo_valor
        elif(categoria==9):
            novo_valor=input('Nova localização: ')
            servico[id_servico]['Localização'] = novo_valor
        else:
            print('Opção Inválida')
            continue
        while True:
            try:
                op = int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não\n'))
                if(op == 1 or op == 2):
                    break
                else:
                    print('Opção Inválida.')
            except:
                print("Valor Inválido.\nDigite apenas números.")
        if(op == 2):
            print('Valor alterado e salvo.')
            break
        elif(op == 1):
            print('Voltando...')


def relatorio_servico(servico):
    tamanho=len(servico)
    if(tamanho==0):
        print('Nenhum serviço cadastrado.')
    else:
        for chave, valor in servico.items():
            if isinstance(valor, dict):
                print(f'\n{chave}')
                relatorio_servico(valor)
            else:
                print(f'{chave}: {valor}')





#Funções das contas a pagar
def cadastro_conta_pagar():
    print('---Digite as informações da Conta---')
    while True:
        try:
            id_conta_pagar=int(input('ID: '))
            if id_conta_pagar in conta_pagar:
                print('ID já cadastrado. Por favor, escolha outro ID.')
            else:
                break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    while True:
        try:
            numero_conta=int(input('Número da conta: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    data_emissao=input('Data da emissão: ')
    data_vencimento=input('Data do vencimento:')
    while True:
        try:
            valor=int(input('Valor a ser pago: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    nome_empresa=input('Nome da empresa ou entidade que emitiu a conta: ')
    endereco_empresa=input('Endereço da empresa:')
    while True:
        try:
            numero_contato=int(input('Telefone de contato: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    email=input('Email de contato: ')
    while True:
        try:
            cnpj=int(input('CNPJ: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    nome_responsavel=input('Nome do responsável pelo pagamento: ')
    endereco_responsavel=input('Endereço do responsável: ')
    while True:
        try:
            cpf=input('CPF do responsável: ')
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    conta_pagar[id_conta_pagar]={'ID':id_conta_pagar,
                                 'Número da conta':numero_conta,
                                 'Data de emissão':data_emissao,
                                 'Data de vencimento':data_vencimento,
                                 'Valor':valor,
                                 'Nome da empresa':nome_empresa,
                                 'Endereço empresa':endereco_empresa,
                                 'Número de contato':numero_contato,
                                 'Email':email,
                                 'CNPj':cnpj,
                                 'Nome do responsável':nome_responsavel,
                                 'Endereço responsável':endereco_responsavel,
                                 'CPF':cpf}


def excluir_conta_pagar():
    while True:
        try:
            id_conta_pagar=int(input('Digite o ID da conta: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    if(id_conta_pagar in conta_pagar):
        del conta_pagar[id_conta_pagar]
        print('Conta excluida.')
    else:
        print('Não existe uma conta com esse ID.')


def alterar_conta_pagar(id_conta_pagar):
    print('--- Alteração da Dados da Conta ---')
    while True:
        while True:
            try:
                categoria = int(input('Escolha a categoria que será alterada:\n1-Nome\n2-CPF\n3-Data de nascimento\n4-Bairro\n5-Rua\n6-Número para contato\n7-Email\n8-sair\n'))
                break
            except:
                print("Valor Inválido.\nDigite apenas números.")        
        if(categoria==1):
            while True:
                try:
                    novo_valor = int(input('Novo Número da conta: '))
                    break
                except:
                    print("Valor Inválido.\nDigite apenas números.")
            conta_pagar[id_conta_pagar]['Número da conta'] = novo_valor
        elif(categoria==2):
            novo_valor=input('Nova data de emissão: ')
            conta_pagar[id_conta_pagar]['Data de Emissão'] = novo_valor
        elif(categoria==3):
            novo_valor = input('Nova data de vencimento: ')
            conta_pagar[id_conta_pagar]['Data de vencimento'] = novo_valor
        elif(categoria==4):
            while True:
                try:
                    novo_valor = int(input('Novo Valor: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números')
            conta_pagar[id_conta_pagar]['Valor'] = novo_valor
        elif(categoria==5):
            novo_valor = input('Novo Nome da empresa: ')       
            conta_pagar[id_conta_pagar]['Nome da empresa'] = novo_valor
        elif(categoria==6):
            novo_valor = input('Novo Endereço da empresa')
            conta_pagar[id_conta_pagar]['Endereço empresa'] = novo_valor
        elif(categoria==7):
            while True:
                try:
                    novo_valor = int(input('Novo Número de contato: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            conta_pagar[id_conta_pagar]['Número de contato'] = novo_valor
        elif(categoria==8):
            novo_valor=input('Novo Email: ')
            conta_pagar[id_conta_pagar]['Email'] = novo_valor
        elif(categoria==9):
            while True:
                try:
                    novo_valor=int(input('Novo CNPJ: '))
                    break
                except:
                    print('Valor inválido.\nDigite apenas números.')
            conta_pagar[id_conta_pagar]['CNPJ'] = novo_valor
        elif(categoria==10):
            novo_valor=input('Novo Nome responsável pelo pagamento:')
            conta_pagar[id_conta_pagar]['Nome do responsável']=novo_valor
        elif(categoria==11):
            novo_valor=input('Novo endereço do responsável: ')
            conta_pagar[id_conta_pagar]['Endereço responsável']=novo_valor
        elif(categoria==12):
            while True:
                try:
                    novo_valor=int(input('Novo CPF: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apnas números.')
            conta_pagar[id_conta_pagar]['CPF']=novo_valor
        else:
            print('Opção Inválida')
            continue
        while True:
            try:
                op = int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não\n'))
                if(op == 1 or op == 2):
                    break
                else:
                    print('Opção Inválida.')
            except:
                print("Valor Inválido.\nDigite apenas números.")
        if(op == 2):
            print('Valor alterado e salvo.')
            break
        elif(op == 1):
            print('Voltando...')


def relatorio_conta_pagar(conta_pagar):
    tamanho=len(conta_pagar)
    if(tamanho==0):
        print('Nenhum conta cadastrada.')
    else:
        for chave, valor in conta_pagar.items():
            if isinstance(valor, dict):
                print(f'\n{chave}')
                relatorio_conta_pagar(valor)
            else:
                print(f'{chave}: {valor}')





#Funções do Veículo
def cadastro_veiculo():
    while True:
        try:
            id_veiculo=int(input('ID: '))
            if id_veiculo in veiculo:
                print('ID já cadastrado. Por favor, escolha outro ID.')
            else:
                break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    marca=input('Marca: ')
    modelo=input('Modelo: ')
    ano_fabricacao=input('Ano de fabricação: ')
    versao=input('Versão: ')
    while True:
        try:
            numero_chassi=int(input('Número do Chassi: '))
            break
        except:
            print('Valor Inválido.\nDigite apenas números')
    placa=input('Placa: ')
    while True:
        try:
            renavam=int(input('RENAVAM: '))
            break
        except:
            print('Valor Inválido.\nDigite apenas números')
    while True:
        try:
            quilometragem=int(input('Quilometragem: '))
            break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    cambio=input('Câmbio: ')
    veiculo[id_veiculo]={'ID':id_veiculo,
                         'Marca':marca,
                         'Modelo':modelo,
                         'Ano de fabricação':ano_fabricacao,
                         'Versão':versao,
                         'Número do Chassi':numero_chassi,
                         'Placa':placa,
                         'RENAVAM':renavam,
                         'Quilometragem':quilometragem,
                         'Câmbio':cambio}
    

def excluir_veiculo():
    while True:
        try:
            id_veiculo=int(input('Digite o ID do veículo: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    if(id_veiculo in veiculo):
        del veiculo[id_veiculo]
        print('Veículo excluido.')
    else:
        print('Não existe um veículo com esse ID.')


def alterar_veiculo(id_veiculo):
    print('--- Alteração da Dados do Veículo ---')
    while True:
        while True:
            try:
                categoria = int(input('Escolha a categoria que será alterada:\n1-Nome\n2-CPF\n3-Data de nascimento\n4-Bairro\n5-Rua\n6-Número para contato\n7-Email\n8-sair\n'))
                break
            except:
                print("Valor Inválido.\nDigite apenas números.")
        if(categoria==1):
            novo_valor=input('Nova Marca: ')
            veiculo[id_veiculo]['Marca']=novo_valor
        elif(categoria==2):
            novo_valor=input('Novo Modelo: ')
            veiculo[id_veiculo]['Modelo']=novo_valor
        elif(categoria==3):
            novo_valor=input('Novo Ano de fabricação: ')
            veiculo[id_veiculo]['Ano de fabricação']=novo_valor
        elif(categoria==4):
            novo_valor=input('Nova Versão:')
            veiculo[id_veiculo]['Versão']=novo_valor
        elif(categoria==5):
            while True:
                try:
                    novo_valor=int(input('Novo Número do Chassi: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            veiculo[id_veiculo]['Número do Chassi']=novo_valor
        elif(categoria==6):
            while True:
                try:
                    novo_valor=int(input('Nova Placa: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            veiculo[id_veiculo]['Placa']=novo_valor
        elif(categoria==7):
            while True:
                try:
                    novo_valor=int(input('Novo RENAVAM: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            veiculo[id_veiculo]['RENAVAM']=novo_valor
        elif(categoria==8):
            while True:
                try:
                    novo_valor=int(input('Nova Quilometragem: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            veiculo[id_veiculo]['Quilometragem']=novo_valor
        elif(categoria==9):
            novo_valor=input('Novo Câmbio: ')
            veiculo[id_veiculo]['Câmbio']
        else:
            print('Opção Inválida')
            continue
        while True:
            try:
                op = int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não\n'))
                if(op == 1 or op == 2):
                    break
                else:
                    print('Opção Inválida.')
            except:
                print("Valor Inválido.\nDigite apenas números.")
        if(op == 2):
            print('Valor alterado e salvo.')
            break
        elif(op == 1):
            print('Voltando...')


def relatorio_veiculo(veiculo):
    tamanho=len(veiculo)
    if(tamanho==0):
        print('Nenhum veículo cadastrado.')
    else:
        for chave, valor in veiculo.items():
            if isinstance(valor, dict):
                print(f'\n{chave}')
                relatorio_veiculo(valor)
            else:
                print(f'{chave}: {valor}')





#Funções do Fornecedor
def cadastro_fornecedor():
    print('---Digite as informações do fornecedor---')
    while True:
        try:
            id_fornecedor=int(input('ID: '))
            if id_fornecedor in fornecedor:
                print('ID já cadastrado. Por favor, escolha outro ID.')
            else:
                break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    nome_empresa=input('Nome da empresa: ')
    horario=input('Horários de atendimento: ')
    endereco_empresa=input('Endereço da empresa: ')
    while True:
        try:
            numero_contato=int(input('Número de contato: '))
            break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    email=input('Email: ')
    website=input('Website: ')
    while True:
        try:
            cnpj=int(input('CNPJ: '))
            break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    produto_serviço=input('Produto/Serviço: ')
    while True:
        try:
            valor=int(input('Valor: '))
            break
        except:
            print('Valor Inválido.\nDigite apenas números.')
    fornecedor[id_fornecedor]={'ID':id_fornecedor,
                               'Nome da empresa':nome_empresa,
                               'Horário de atendimento':horario,
                               'Endereço da empresa':endereco_empresa,
                               'Número de conato':numero_contato,
                               'Email':email,
                               'Website':website,
                               'CNPJ':cnpj,
                               'Produto/Serviço':produto_serviço,
                               'Valor':valor}
    

def excluir_fornecedor():
    while True:
        try:
            id_fornecedor=int(input('Digite o ID do fornecedor: '))
            break
        except:
            print("Valor Inválido.\nDigite apenas números.")
    if(id_fornecedor in fornecedor):
        del fornecedor[id_fornecedor]
        print('Fornecedor excluido.')
    else:
        print('Não existe um fornecedor com esse ID.')


def alterar_fornecedor(id_fornecedor):
    print('--- Alteração da Dados do Fornecedor ---')
    while True:
        while True:
            try:
                categoria = int(input('Escolha a categoria que será alterada:\n1-Nome\n2-CPF\n3-Data de nascimento\n4-Bairro\n5-Rua\n6-Número para contato\n7-Email\n8-sair\n'))
                break
            except:
                print("Valor Inválido.\nDigite apenas números.")
        if(categoria==1):
            novo_valor=input('Novo Nome da empresa: ')
            fornecedor[id_fornecedor]['Nome da empresa']=novo_valor
        elif(categoria==2):
            novo_valor=input('Novo Horário de atendimento: ')
            fornecedor[id_fornecedor]['Horário de atendimento']=novo_valor
        elif(categoria==3):
            novo_valor=input('Novo Endereço da empresa: ')
            fornecedor[id_fornecedor]['Endereço da empresa']=novo_valor
        elif(categoria==4):
            while True:
                try:
                    novo_valor=int(input('Novo Número de contato: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            fornecedor[id_fornecedor]['Número de contato']=novo_valor
        elif(categoria==5):
            novo_valor=input('Novo Email: ')
            fornecedor[id_fornecedor]['Email']=novo_valor
        elif(categoria==6):
            novo_valor=input('Novo Website: ')
            fornecedor[id_fornecedor]['Website']=novo_valor
        elif(categoria==7):
            while True:
                try:
                    novo_valor=int(input('Novo CNPJ: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            fornecedor[id_fornecedor]['CNPJ']=novo_valor
        elif(categoria==8):
            novo_valor=input('Novo Produto/Serviço: ')
            fornecedor[id_fornecedor]['Produto/Serviço']=novo_valor
        elif(categoria==9):
            while True:
                try:
                    novo_valor=float(input('Novo Valor: '))
                    break
                except:
                    print('Valor Inválido.\nDigite apenas números.')
            fornecedor[id_fornecedor]['Valor']=novo_valor
        else:
            print('Opção Inválida')
            continue
        while True:
            try:
                op = int(input('Gostaria de alterar algo mais?\n1-Sim        2-Não\n'))
                if(op == 1 or op == 2):
                    break
                else:
                    print('Opção Inválida.')
            except:
                print("Valor Inválido.\nDigite apenas números.")
        if(op == 2):
            print('Valor alterado e salvo.')
            break
        elif(op == 1):
            print('Voltando...')


def relatorio_fornecedor(fornecedor):
    tamanho=len(fornecedor)
    if(tamanho==0):
        print('Nenhum fornecedor cadastrado.')
    else:
        for chave, valor in fornecedor.items():
            if isinstance(valor, dict):
                print(f'\n{chave}')
                relatorio_fornecedor(valor)
            else:
                print(f'{chave}: {valor}')