"""faça um prog que leia um angulo e mostre
o valor do seno, cossenoe e tangente
"""
import math
angle = float(input('Digite o valor do angulo: '))

sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tg = math.tan(math.radians(angle))

print('O angulo {}, tem:\n'
      'seno igual a = {:.2f}\n'
      'cosseno igual a = {:.2f}\n'
      'tangente igual a = {:.2f}'.format(angle, sen, cos, tg))