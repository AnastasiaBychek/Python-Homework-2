N = input("Input number")
c = N.split(".")
a = int(c[0])
b = int(c[1])
sum = 0
while a!=0:
    sum = sum +a%10
    a = a//10
while b!=0:
    sum = sum +b%10
    b = b//10
print(a)
print(b)
print(sum)

