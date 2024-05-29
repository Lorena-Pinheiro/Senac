"""numeros=[17,123,87,34,66,8398,44]
print(numeros[2])
print(numeros[9-8])
print(numeros[-2])
print(numeros[-1])
print(numeros[5][1])"""

#fala se o elemento está na lista 
"""frutas=["maca","laranja","cereja","banana"]
print("maca" in frutas)
print("pera" in frutas)"""

"""print([1,2]+[3,4])
print(frutas+[6,7,8,9])"""

"""print(["teste"]*4)
print([1,2,["ola","adeus"]]*2)"""

#mostra o maior e o menor elemento de uma lista
"""a=[1,2,3,4,5,6,7,8,9]
print(a)
print(max(a))
print(min(a))
print(sum(a))"""

"""uma_lista=['a','b','c','d','e','f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])
print(uma_lista[0:6])"""

#substiui um elemento da lista por outro
"""uma_lista=['a','b','c','d','e','f']
uma_lista[1:1]=['x','y']
print(uma_lista)"""

"""uma_lista=['a','b','c','d','e','f']
uma_lista[1:1]=['b','c']
print(uma_lista)
uma_lista[4:4]=['e']
print(uma_lista)"""

#deleta um elemento da lista
"""a=['um','dois','três']
del a[1]
print(a)
lista=['a','b','c','d','e','f']
del lista[1:5]
print(lista)"""

#acrescenta um elemento no final da lista
"""a=[81,82,83]
a.append(5)
print(a)"""

#organiza a lista
"""a=[88,81,82,83]
a.sort()
print(a)
a=[88,81,82,83]
a.sort(reverse=True)
print(a)"""

#mostra o index do elemento pesquisado
"""a=[1,2,3,4,5,6,7,8,9]
print(a.index(4))"""

#acrescenta um elemento à lista na posição escolhida
"""a=[88,81,82,83]
a.insert(1,100)
print(a)"""

#conta quantas vezes um elemento aparece na lista
"""a=[88,81,82,83,88,85,88,86]
print(a)
print(a.count(88))"""

#apaga o ultimo elemento da lista ou algum elemento escolhido
"""a=[88,81,82,83,88,85,88,86]
a.pop()
print(a)
a.pop(0)
print(a)"""


"""idade=18
if(idade<20):
    print("Você é jovem")
print("Fim.Fora do if")"""

"""idade(int(input()))
if (idade >=16 and idade<18):
    print("Pode votar")
elif(idade<16):
    print("Apenas estude")
else:
    print("Pode dirigir")"""

"""n1,n2=map(int,input("Digite dois números: ").split())
if(n1>n2):
    print(f"{n1} é maoir que {n2}")
else:
    print(f"{n2} é maoir que {n1}")"""

"""n1=int(input("Digite um número: "))
if(n1<0):
    print(f"{n1} é um número negativo")
elif(n1>0):
    print(f"{n1} é um número positivo")
else:
    print(f"{n1} é um número neutro")"""

"""n1,n2=map(int,input("Digite as duas notas: ").split())
media=(n1+n2)/2
if(media>=7):
    print("Aprovado")
else:
    ("Reprovado")"""

"""salario=int(input("Digite o seu salário: "))
if(salario<500):
    salario_reajustado=salario+15/100
    print(f"Novo salário: R${salario_reajustado}")
elif(salario>=500 and salario<=1000):
    salario_reajustado=salario*(10/100)
    print(f"Novo salário: R${salario_reajustado}")
elif(salario>1000):
    salario_reajustado=salario*(5/100)
    print(f"Novo salário: R${salario_reajustado}")"""

"""letra=input("Digite uma letra: ")
if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U"):
    print("A letra digitada foi uma vogal")
else:
    print("A letra digitada foi uma consoante")"""

"""n1,n2=map(int,input("Digite as duas notas: ").split())
media=(n1+n2)/2
if(media>=7):
    print("Aprovado")
elif(media==10):
    print("Aprovado com distinçaõ")
else:
    ("Reprovado")"""

"""n1,n2,n3=map(int,input("Digite três números: ").split())
if(n1>n2 and n1>n3):
    print(f"{n1} é o maior")
elif(n2>n1 and n2>n3):
    print(f"{n2} é o maior")
elif(n3>n1 and n3>n2):
    print(f"{n3} é o maior")"""

"""v1,v2,v3=map(float,input("Informe o valor dos três produtos: ").split())
if(v1>v2 and v1>v3):
    print("O produto 1 é o mais barato")
elif(v2>v1 and v2>v3):
    print("O produto 2 é o mais barato")
elif(v3>v1 and v3>v2):
    print("O produto 3 é o mais barato")"""

"""salario=int(input("Informe o seu salário: "))
if(salario<280):
    aumento=1.20*salario
    valor_aumento=aumento-salario
    print(f"Salário antes do reajuste: R${salario}\nPercentual de aumento aplicado: 20%\nValor do aumento: RS{valor_aumento}\nNovo salário: R${aumento}")
elif(salario>=280 or salario<700):
    aumento=1.15*salario
    valor_aumento=aumento-salario
    print(f"Salário antes do reajuste: R${salario}\nPercentual de aumento aplicado: 15%\nValor do aumento: RS{valor_aumento}\nNovo salário: R${aumento}")
elif(salario>=700 or salario<1500):
    aumento=1.10*salario
    valor_aumento=aumento-salario
    print(f"Salário antes do reajuste: R${salario}\nPercentual de aumento aplicado: 10%\nValor do aumento: RS{valor_aumento}\nNovo salário: R${aumento}")
elif(salario>1500):
    aumento=1.05*salario
    valor_aumento=aumento-salario
    print(f"Salário antes do reajuste: R${salario}\nPercentual de aumento aplicado: 5%\nValor do aumento: RS{valor_aumento}\nNovo salário: R${aumento}")"""

"""print("Telefonou para a vítima? Se Sim digite 1 se Não digite 0")
p1=int(input())
print("Esteve no local do crime? Se Sim digite 1 se Não digite 0")
p2=int(input())
print("Mora perto da vítima? Se Sim digite 1 se Não digite 0")
p3=int(input())
print("Devia para a vítima? Se Sim digite 1 se Não digite 0")
p4=int(input())
print("Já trabalhou com a vítima? Se Sim digite 1 se Não digite 0")
p5=int(input())
total=p1+p2+p3+p4+p5
if(total==2):
    print("Suspeita")
elif(total==3 or total==4):
    print("Cúmplice")
elif(total==5):
    print("Assassino")
else:
    print("Inocente")"""


"""quantidade=float(input("Digite a quantidade em kg: "))
tipo=input("Digite o tipo da carne: ")
if(quantidade<=5):
    if(tipo=="File Duplo"):
        pagamento=input("Como deseja pagar?: ")
        if(pagamento=="Tabajara" or pagamento=="tabajara"):
            preco_total=quantidade*4.90
            desconto=preco_total*0.05
            preco_desconto=preco_total-desconto
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R${desconto}\nValor a Pagar: {preco_desconto}")
        else:
            preco_total=quantidade*4.90
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R$0\nValor a Pagar: {preco_total}")
    elif(tipo=="Alcatra"):
        pagamento=input("Como deseja pagar?: ")
        if(pagamento=="Tabajara" or pagamento=="tabajara"):
            preco_total=quantidade*5.90
            desconto=preco_total*0.05
            preco_desconto=preco_total-desconto
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R${desconto}\nValor a Pagar: {preco_desconto}")
        else:
            preco_total=quantidade*5.90
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R$0\nValor a Pagar: {preco_total}")
    elif(tipo=="Picanha"):
        pagamento=input("Como deseja pagar?: ")
        if(pagamento=="Tabajara" or pagamento=="tabajara"):
            preco_total=quantidade*6.90
            desconto=preco_total*0.05
            preco_desconto=preco_total-desconto
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R${desconto}\nValor a Pagar: {preco_desconto}")
        else:
            preco_total=quantidade*6.90
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R$0\nValor a Pagar: {preco_total}")
elif(quantidade>5):
    if(tipo=="File Duplo"):
        pagamento=input("Como deseja pagar?: ")
        if(pagamento=="Tabajara" or pagamento=="tabajara"):
            preco_total=quantidade*5.80
            desconto=preco_total*0.05
            preco_desconto=preco_total-desconto
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R${desconto}\nValor a Pagar: {preco_desconto}")
        else:
            preco_total=quantidade*5.80
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R$0\nValor a Pagar: {preco_total}")
    elif(tipo=="Alcatra"):
        pagamento=input("Como deseja pagar?: ")
        if(pagamento=="Tabajara" or pagamento=="tabajara"):
            preco_total=quantidade*6.80
            desconto=preco_total*0.05
            preco_desconto=preco_total-desconto
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R${desconto}\nValor a Pagar: {preco_desconto}")
        else:
            preco_total=quantidade*6.80
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R$0\nValor a Pagar: {preco_total}")
    elif(tipo=="Picanha"):
        pagamento=input("Como deseja pagar?: ")
        if(pagamento=="Tabajara" or pagamento=="tabajara"):
            preco_total=quantidade*7.80
            desconto=preco_total*0.05
            preco_desconto=preco_total-desconto
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R${desconto}\nValor a Pagar: {preco_desconto}")
        else:
            preco_total=quantidade*7.80
            print(f"Tipo de carne: {tipo}\nQuantidade de carne: {quantidade}\nPreço Total:{preco_total}\nTipo de pagamento: {pagamento}\nValor do Desconto: R$0\nValor a Pagar: {preco_total}")"""

"""while True:
    valor=int(input("Digite o valor 1 ou 0 para encerrar "))
    if(valor==1):
        print("Valor correto")
    else:
        print("Valor para sair")
        break"""

"""while True:
    valor=int(input("Digite o valor 1 ou 0 para encerrar "))
    if(valor==1):
        continue
        print("Valor correto")
    else:
        print("Valor para sair")""" 

#Dicionario
"""tradutor= {}
tradutor ["pineapple"]="abacaxi"
tradutor["apple"]="maça"
tradutor["oranje"]="laranja"
print(type(tradutor))
print(tradutor)"""

"""tradutor1={}
tradutor1={"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print(tradutor1["apple"])"""

tradutor1={}
tradutor1={"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print(tradutor1)
del(tradutor1["apple"])
print(tradutor1)
print(tradutor1.pop("banana","Fruta não encontrada"))
tradutor1.clear()
print(tradutor1)