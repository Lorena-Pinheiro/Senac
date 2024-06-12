def valorPagamento(prestacao,dias_atraso):
    if(dias_atraso==0):
        valorTotal=prestacao
        return valorTotal
    else:
        multa=prestacao*3/100
        juros=(prestacao*0.1/100)*dias_atraso
        valorTotal=prestacao+multa+juros
        return valorTotal

i=0
valorTotal=0
while True:
    prestacao=int(input('Informe o valor da prestação: '))
    dias_atraso=int(input('informe a quantidade de dias de atraso: '))
    if(prestacao!=0):
        valorTotal+=valorPagamento(prestacao,dias_atraso)
    else:
        print(f"Quantidade de prestações pagas: {i}\nValor Total: {valorTotal}")
        break
    i+=1