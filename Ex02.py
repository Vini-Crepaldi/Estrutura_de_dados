#entrada pelo teclado

salario_fixo = 500.00
vendas = float(input("Digite o valor das vendas do mês: R$ "))
comissao = vendas * 0.06
faturamento_total = salario_fixo + comissao

print(f"Faturamento total: R$ {faturamento_total:.2f}")
