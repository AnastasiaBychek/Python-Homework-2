N = int(input("Input number"))
from random import randint
list = []
for i in range(N):
    list.append(randint(-N,N+1))
print(list)
a = int(input(f"Input index a from range [0,{N-1}]"))
b = int(input(f"Input index b from range [0,{N-1}]"))
print(list[a])
print(list[b])
print(list[a]+list[b])