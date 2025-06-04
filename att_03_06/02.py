n = int(input("Digite a quantidade de termos (mínimo 2): "))
while n < 2:
    n = int(input("Valor inválido. Digite um número maior ou igual a 2: "))

fibonacci = [0, 1]

for i in range(2, n):
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

print("Sequência de Fibonacci:", fibonacci)
