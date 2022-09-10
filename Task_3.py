N = int(input("Input number"))
a =[]
for i in range(1,N+1):
    a.append(round((1+1/i)**i,3))
print(sum(a))