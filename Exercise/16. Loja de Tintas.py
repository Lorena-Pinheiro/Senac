area_pintada=int(input("Informe o tamanho em metros da área a ser pintada: "))
litro=area_pintada/3
lata=int(litro/18)
preco=lata*80
print("Você usara {} latas de tinta\nPreço total: {}".format(lata,preco))