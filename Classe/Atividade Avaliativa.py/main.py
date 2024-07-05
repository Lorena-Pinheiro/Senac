from Policial import *
from BO import *
from Preso import *

while True:
    
    while True:
        try:
            op = int(input("--- Menu ---\n1-Cadastro\n2-Relatórios\n3-Sair\n"))
            break
        except:
            print("Valor Inválido")
            
    if(op == 1):
        while True:
            try:
                op2 = int(input("--- Cadastro ---\n1-Policial\n2-BO\n3-Preso\n4-Sair\n"))
                break
            except:
                print("Valor Inválido")
        if(op2 == 1):
            print("--- Policial ---")
            policial = Policial()
            policial.cadastro_Policial()
        elif(op2 == 2):
            print("--- BO ----")
            bo = BO()
            bo.cadastro_BO()
        elif(op2 == 3):
            print("--- Preso ---")
            preso = Preso()
            preso.cadastro_Preso()
            
    elif(op == 2):
        while True:
            try:
                op2 = int(input("--- Relatório ---\n1-Policial\n2-BO\n3-Preso\n4-Sair\n"))
                break
            except:
                print("Valor Inválido")
        if(op2 == 1):
            print("--- Policial ---")
            policial.relatorio_Policial()
        elif(op2 == 2):
            print("--- BO ---")
            bo.relatorio_BO()
        elif(op2 == 3):
            print("--- Preso ---")
            preso.relatorio_Preso()
        elif(op2 == 4):
            break
    
    elif(op == 3):
        break
    
    else: 
        print("Opção Inválida")