def Soma(*valores):
    r= 0
    for i in valores:
            r+= i
    return r

print(Soma(3,9))
print(Soma(1,2,3,4))
print(Soma())
print(Soma(5))