# 1º input string dia da semana
# 2º input nro natual 0 a 6

dia_compra = input()
prazo = int(input())

if dia_compra == 'domingo':
  dia_nro = 0
elif dia_compra == 'segunda':
  dia_nro = 1
elif dia_compra == 'terca':
  dia_nro = 2
elif dia_compra == 'quarta':
  dia_nro = 3
elif dia_compra == 'quinta':
  dia_nro = 4
elif dia_compra == 'sexta':
  dia_nro = 5
elif dia_compra == 'sabado':
  dia_nro = 6

dia_entrega = dia_nro + prazo
if dia_entrega > 6:
  dia_entrega = dia_entrega - 7

if prazo == 0:
  print ('chega hoje!')
elif dia_entrega == 0:
  print ('sera entregue domingo')
elif dia_entrega == 1:
  print ('sera entregue segunda')
elif dia_entrega == 2:
  print ('sera entregue terca')
elif dia_entrega == 3:
  print ('sera entregue quarta')
elif dia_entrega == 4:
  print ('sera entregue quinta')
elif dia_entrega == 5:
  print ('sera entregue sexta')
elif dia_entrega == 6:
  print ('sera entregue sabado')