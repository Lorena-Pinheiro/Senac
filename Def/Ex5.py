import random
def embaralhar(palavra):
    p=list(palavra)
    random.shuffle(p)
    print(''.join(p))

palavra=input("Digite uma palavra: ")
embaralhar(palavra)