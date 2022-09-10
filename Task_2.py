N = int(input("Input number"))
a = [1]
factorial = 1
for i in range(2,N+1):
    factorial *= i
    a.append(factorial)
print(a)
