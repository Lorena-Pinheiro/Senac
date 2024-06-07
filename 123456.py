"""import os

nome=input("Digite o seu nome: ")
os.system('cls')
print("O seu nome está certo? ",nome)
os.system('pause')
os.system('cls')"""

import math
"""x=3.5
print(math.ceil(x))"""

"""x=-3
print(math.fabs(x))"""

"""x=3
print(math.factorial(x))"""

"""x=3.5
print(math.floor(x))"""

"""x=2
y=10

print(math.pow(x,y))"""

import datetime

""""print(datetime.date.today().strftime('%d/%m/%Y'))

print(datetime.date.today().strftime('%d/%m/%Y %H:%M'))"""

import time

a=0
x=time.perf_counter()
while a<10000:
    print(a)
    a+=1
y=time.perf_counter()
print(y-x)