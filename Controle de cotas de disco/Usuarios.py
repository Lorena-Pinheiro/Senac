usuarios = {}

class Usuario:
    
    def __init__(self,login=None,espaco_disco=None):
        self.login = login
        self.espaco_disco = espaco_disco
        
    def cadastro_usuario(self):
        self.login = input("Digite o Login do Usuário: ")
        while True:
            try:
                self.espaco_disco = int(input("Digite o espaço em disco ocupado pelo diretótio home do Usuário: "))
                break
            except:
                print("Valor Inválido. Digite apenas números.")
        usuarios[self.login] = self.espaco_disco
        
    def relatorio(self,mgb,porcentagem):
        espaco_total = sum(usuarios.values())
        espaco_medio = espaco_total / len(usuarios)
        print("ACME Inc.            Uso do espaço em disco pelos usuários","-" * 70,"\nNr. Usuário      Espaço utilizado        % do uso")
        
        n = 1
        for self.login in usuarios:
            print(f"{n}     {self.login}        {mgb}       {porcentagem}")
            n += 1
            
        print(f"\nEspaço total ocupado: {espaco_total} MB")
        print(f"Espaço médio ocupado: {espaco_medio} MB")