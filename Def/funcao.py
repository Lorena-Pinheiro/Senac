#Dicionarios
cliente={}
peca={}
serviço={}
conta_pagar={}
veiculo={}
fornecedor={}


#Funções do Cliente
def cadastro_cliente():
    print('---Informe as informações do cliente---')
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
#def alterar_cliente(,categoria,novo_valor):
    

    

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
    data_fabriacao=input('Data de fabricação: ')
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
    peca[numero_peca]={'nome':nome,'marca':marca,'data_fabricacao':data_fabricacao,}

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