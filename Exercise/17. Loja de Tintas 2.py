area_pintada=int(input("Informe o tamanho em metros da área a ser pintada: "))
folga=area_pintada*1.1
litro=folga/6

lata=int(litro/18)
preco_lata=lata*80

galao=int(litro/3.6)
preco_galao=galao*25

mistura_galao=litro-lata
preco_mistura=lata*80+mistura_galao*25
print("Apenas latas: R$ %s\nApenas galões: R$ %s\nLatas e Galões: R$%s"%(preco_lata,preco_galao,preco_mistura))