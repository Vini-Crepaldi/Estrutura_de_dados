def Operacoes (x, y):
    ad = x + y
    su = x - y
    mu = x * y
    di = x / y
    return ad,su,mu,di

print ("inicio do programa")
a = int(input(" digite  um valor para a"))
b = int(input(" digite  um valor para b"))
s=  Operacoes(a,b)
print(s)
print()
print("fim")