l = []
p = (12336, 'Sabao', 1337, 1.37)
l.append(p)
p = (123345, 'arroz 1kg', 342, 2.65)
l.append(p)
P = (123345, 'arroz 1kg', 342, 2.65)
l.append(p)

for(cod,nome,qtd,nsei) in l:
    print('indentificação de produto:', cod)
    print('descrição', nome)
    print('estoque', qtd)
    print('estoque = {0} e R$ {1:.2f}'.format (qtd,nsei))
    print('total = R$ {0:.2f}'.format(qtd * nsei))
    print()
print('fim')