def reverso(numero):
    num=list(numero)
    num.sort(reverse=True)
    print(''.join(num))

n=input("Digite um número: ")
reverso(n)
