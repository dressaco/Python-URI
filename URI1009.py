nome = input()
salario_fixo = float(input())
vendas_mes = float(input())

comissao = vendas_mes * 0.15
salario_total = salario_fixo + comissao

print(f'TOTAL = R$ {salario_total:.2f}')