import random

d20=random.randrange(1,21)
print(d20)

x=random.uniform(1.5,2.1)
print(x)

sorteador_grupo=random.choice(['Grupo1:','Grupo2:','Grupo3:'])
print(sorteador_grupo)

sorteador_grupo=random.choice(['Grupo1:','Grupo2:','Grupo3:'])
nomes=(['Juvenal','James','Xaropinho','Seraphyne','Juvencyo','Ladislau'])
nomes_sorteados=random.sample(nomes,2)
print(sorteador_grupo,', '.join(nomes_sorteados))