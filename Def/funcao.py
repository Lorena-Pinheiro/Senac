#Dicionarios
cliente={}
peca={}
servico={}
conta_pagar={}
veiculo={}
fornecedor={}


#Funções do Cliente
def cadastro_cliente():
    print('---Informe as informações do cliente---')
    while True:
        id_cliente=int(input('ID: '))
        if(id_cliente != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    nome=input('Nome: ')
    while True:
        cpf=int(input('CPF: '))
        if(cpf in cliente):
            print('CPF já cadastrado.\nDigite outro.')
        elif(cpf != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    data_nascimento=input('Data de nascimento: ')
    bairro=input('Bairro: ')
    rua=input('Rua: ')
    while True:
        numero_contato=int(input('Número para contato: '))
        if(numero_contato != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    email=input('Email: ')
    cliente[cpf]={'nome':nome,'data_nascimento':data_nascimento,'bairro':bairro,'rua':rua,'numero_contato':numero_contato,'email':email}
    
def excluir_cliente():
    while True:
        cpf=int(input('Digite o CPF do cliente: '))
        if(cpf!=int):
            print('CPF inválido.')
        else:
            break
    if(cpf in cliente):
        del cliente[cpf]
        print('Cliente excluido.')
    else:
        print('Não existe um cliente com esse CPF.')

def alterar_cliente(cpf,categoria,novo_valor):
    while True:
        while True:
            cpf=int(input('Digite o CPF do cliente: '))
            if(cpf!=int):
                print("Valor Inválido.\nDigite apenas números.")
            elif(cpf not in cliente):
                print('Cliente não cadastrado.')
            else:
                break
        categoria=input('Digite a categoria que será alterada: ')
        if(categoria=='cpf'):
            novo_valor=int(input('Digite o novo valor: '))
            cliente[cpf][categoria]=novo_valor
        else:
            novo_valor=input('Digite o novo valor: ')
            cliente[cpf][categoria]=novo_valor
    
def relatorio_cliente():
    print(cliente)
    



#Funções da Peça
def cadastro_peca():
    while True:
        numero_peca=int(input('Número: '))
        if (numero_peca in peca):
            print('Número já cadastrado.\nDigite outro.')
        elif(numero_peca != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    nome=input('Nome:')
    marca=input('Marca: ')
    data_fabricacao=input('Data de fabricação: ')
    funcao=input('Função: ')
    while True:
        peso=input('Peso: ')
        if(peso != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    material=input('Material: ')
    while True:
        preco=input('Preço: ')
        if(preco != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    while True:
        quantidade=input('Quantidade em estoque: ')
        if(quantidade != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    localizacao=input('Localização no veículo: ')
    peca[numero_peca]={'nome':nome,'marca':marca,'data_fabricacao':data_fabricacao,'funcao':funcao,'peso':peso,'material':material,'preco':preco,'quantidade':quantidade,'localizacao':localizacao}

def excluir_peca():
    while True:
        numero_peca=int(input('Digite o número da peça: '))
        if(numero_peca!=int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    if(numero_peca in cliente):
        del peca[numero_peca]
        print('Peça excluido.')
    else:
        print('Não existe uma peça com esse número.')




#Funções do Serviço
def cadastro_servico():
    while True:
        id_servico=int(input('ID: '))
        if(id_servico != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    tipo_servico=input('Tipo do serviço: ')
    while True:
        custo_maoDeobra=int(input("Custo da mão de obra: "))
        if(custo_maoDeobra != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    peca_usada=input('Peças usadas: ')
    while True:
        custo_peca=int(input('Custo das peças: '))
        if(custo_peca != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    while True:
        valor_total=int(input('Valor total do serviço: '))
        if(valor_total != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    tempo_estimado=input('Tempo estimado do serviço: ')
    tarefa_realizada=input('Tarefas realizadas: ')
    ferramentas_usadas=input('Ferramentas usadas: ')
    
def excluir_servico():
    while True:
        id_servico=int(input('Digite o número da peça: '))
        if(id_servico!=int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    if(id_servico in servico):
        del servico[id_servico]
        print('Serviço excluido.')
    else:
        print('Não existe um serviço com esse ID.')




#Funções das contas a pagar
def cadastro_contas_pagar():
    while True:
        numero_conta=int(input('Número da conta: '))
        if(numero_conta != int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    data_emissao=input('Data da emissão: ')
    data_vencimento=input('Data do vencimento:')
    while True:
        valor=int(input('Valor a ser pago: '))
        if(valor!=int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    nome_empresa=input('Nome da empresa ou entidade que emitiu a conta: ')
    endereco_empresa=input('Endereço da empresa:')
    while True:
        numero_contato=int(input('Telefone de contato: '))
        if(numero_contato!=int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    email=input('Email de contato: ')
    while True:
        cnpj=int(input('CNPJ: '))
        if(cnpj!=int):
            print("Valor Inválido.\nDigite apenas números.")
        else:
            break
    nome_responsavel=input('Nome do responsável pelo pagamento: ')
    endereco_responsavel=input('Endereço do responsável: ')
    cpf=input('CPF: ')