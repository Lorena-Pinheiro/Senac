
while True:
    try:               
        op3=int(input('1-Enviar         2-Editar\n'))
        break
    except:
        print('Valor Inválido.\nDigite apenas números.')
if(op3==1):
    print('Enviando...')
elif(op3!=1 or op3!=2):
    print('Opção Inválida')