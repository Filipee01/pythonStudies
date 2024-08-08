 #operações aritimeticas
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 #divisao inteira
e = n1 ** n2
print('A soma vale: {}, o produto vale: {}, a divisão vale: {:.2f}'.format(s, m, d), end = '')
print('Divisao inteira {} e potencia {}'.format(di, e))