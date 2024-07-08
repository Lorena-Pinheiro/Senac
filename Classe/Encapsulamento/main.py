from ContaBancaria import *

while True:
    op = int(input('--- Menu ---\n1-Cadastro\n2-Saldo\n3-Saque\n4-Deposito\n'))
    if op == 1:
        print('--- Cadastro ---')
        nome = input('Nome: ')
        saldo = int(input('Saldo: '))
        cpf = int(input('CPF: '))
        senha = input('Senha: ')
        conta1 = ContaBancaria(nome,saldo,cpf,senha)
    elif op == 2:
        print('--- Saldo ---')
        senha = input('Digite sua senha: ')
        conta1.extrato(senha)
    elif op == 3:
        print('--- Saque ---')
        valor = int(input('Digite o valor a ser sacado: '))
        senha = input('Digite sua senha: ')
        conta1.sacar(senha,valor)
    elif op == 4:
        print('--- Deposito ---')
        valor = int(input('Digite o valor a ser depositado: '))
        conta1.depositar(valor)
        