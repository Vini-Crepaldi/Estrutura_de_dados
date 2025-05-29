def Soma (x,y):
    r = x + y
    return r


a = int(input("digite um valor para a: " ))
b = int(input("digite um valor para b: " ))
c = int(input("digite um valor para c: " ))

s = Soma(a,b)
print("a + b = {0}".format(s))

s = Soma(a,c)
print("a + c = {0}".format(s))

s = Soma(c,b)
print("c + b = {0}".format(s))

print("")
print("Fim do programa")