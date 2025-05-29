def EstudoEscopo():
    global x
    x = 19
    y = x * 2

    print("x global existe dentro da função com o valor = {0}".format(x))
    print(' y local existe dentro da funcao valor = {0}'.format(y))
print('inicio do programa')
x = 10
print ("x global existe fora da função com o valor {0}".format(x))
EstudoEscopo()
print("x global foi alterado com o valor de {0}".format(x))
print("fim")