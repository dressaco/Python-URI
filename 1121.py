#desc fixo de 10%
#desc var de 1% por unidade

#input nro real valor mercadoria
#input nro int qtde unidades

preco_mercadoria = float(input())
qtd_comprada = int(input())

total = preco_mercadoria * qtd_comprada
desconto = total * (0.10 + qtd_comprada * 0.01)
total_final = total - desconto

print (f'{total:.2f}')
print (f'{total_final:.2f}')