def Soma (x, y =1):
    r = x + y
    return r



print("inicio do programa")
a = int(input(" valor a: "))
b = int(input(" valor b: "))
s = Soma(a,b)
print("a+b = {0} ".format(s))
s = Soma(a,2)
print("a+2 = {0} ".format(s))



print("")
print("fim")