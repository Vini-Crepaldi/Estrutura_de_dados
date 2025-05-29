def EstudoEscopo():
    y = x * 2

    print("x global existe dentro da função com o valor = {0}".format(x))
    print(' y local existe dentro da funcao valor = {0}'.format(y))
print('inicio do programa')
x = 10
print ("x global existe fora da função com o valor {0}".format(x))
EstudoEscopo()
print("fim")