print("Fibonacci")
var = int(input("Digite o valor: "))

# n + 1 = n + n-1

a = 0
b = 1
c = a+b

for n in range (a, var ):
    print (a)
    c = b + a
    a = b
    b = c