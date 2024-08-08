"""crie um programa que leia um numero real qualquer
pelo teclado e mostre sua porção inteira"""
import math
number = float(input('Digite um numero: '))
print('O numero {} de forma inteira ficou: {}'.format(number, math.trunc(number)))

