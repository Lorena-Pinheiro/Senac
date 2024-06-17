def data_extenso(data):
    if (data[3:5] == '01' and data[3:5]<'31' or data[3:5]>'00'):
        print(data[0:2],'de Janeiro de',data[6:])
    elif (data[3:5] == '02' and data[3:5]<'28' or data[3:5]>'00'):
        print(data[0:2],'de Fevereiro de',data[6:])
    elif (data[3:5] == '03' and data[3:5]<'31' or data[3:5]>'00'):
        print(data[0:2],'de Março de',data[6:])
    elif (data[3:5] == '04' and data[3:5]<'30' or data[3:5]>'00'):
        print(data[0:2],'de Abril de',data[6:])
    elif (data[3:5] == '05' and data[3:5]<'31' or data[3:5]>'00'):
        print(data[0:2],'de Maio de',data[6:])
    elif (data[3:5] == '06' and data[3:5]<'30' or data[3:5]>'00'):
        print(data[0:2],'de Junho de',data[6:])
    elif (data[3:5] == '07' and data[3:5]<'31' or data[3:5]>'00'):
        print(data[0:2],'de Julho de',data[6:])
    elif (data[3:5] == '08' and data[3:5]<'31' or data[3:5]>'00'):
        print(data[0:2],'de Agosto de',data[6:])
    elif (data[3:5] == '09' and data[3:5]<'30' or data[3:5]>'00'):
        print(data[0:2],'de Setembro de',data[6:])
    elif (data[3:5] == '10' and data[3:5]<'31' or data[3:5]>'00'):
        print(data[0:2],'de Outubro de',data[6:])
    elif (data[3:5] == '11' and data[3:5]<'30' or data[3:5]>'00'):
        print(data[0:2],'de Novembro de',data[6:])
    elif (data[3:5] == '12' and data[3:5]<'31' or data[3:5]>'00'):
        print(data[0:2],'de Dezembro de',data[6:])
    else:
        return

data=input("Digite uma data: ")
data_extenso(data)