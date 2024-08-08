"""crie um programa que leia o valor em metro
e o exiba convertido em centimetros"""

metro = float(input('Digite um valor em metros para conversão: '))
cm = metro * 100
mm = metro * 1000

print('o valor: {}, convertido em centimetros \n equivale a: {} cm, e esse valor \n '
      'convertido em milimetros equivale a: {} mm'.format(metro, cm, mm))