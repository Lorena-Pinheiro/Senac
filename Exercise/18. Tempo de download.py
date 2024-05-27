tamanho,velocidade=map(int,input("Informe o tamanho do arquivo para download e a velocidade do link: ").split())
tempo=(tamanho/velocidade/8)/60
print("O tempo aproximado é %s minutos"%tempo)