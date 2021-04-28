# input = nro natural >= 2
# resultado1 = nro impar anterior
# resultado2 = nro par posterior

numero = int(input())

if numero % 2 == 0: # se / 2 resto 0, nro par
  print(f'{numero - 1} {numero + 2}')
else: # se resto != 0, nro impar
  print (f'{numero - 2} {numero + 1}')