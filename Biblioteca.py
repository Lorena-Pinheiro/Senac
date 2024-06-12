import numpy as np

x=np.arange(8,15)
print(x)

from fractions import Fraction

a=int(input("Digite um número: "))
b=int(input("Digite um número: "))
c=int(input("Digite um número: "))
d=int(input("Digite um número: "))

frac1= Fraction(a,b)
frac2= Fraction(c,d)

print("A soma das frações é: ",frac1+frac2)

import emoji

resposta=input("Voce esta feliz ou triste? (F/T)")

if resposta.upper() == F:
    print(emoji.emojize("Fico feliz por voce"))


"""import pyautogui

pyautogui.press('win')
pyautogui.typewrite('notepad')
pyautogui.press('enter')

pyautogui.typewrite('Olá')

pyautogui.hotkey('ctrl','s')
pyautogui.typewrite('exemplo.txt')
pyautogui.press('enter')"""