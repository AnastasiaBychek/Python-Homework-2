a = "abababb"
b = "aba"
count = 0
for i in range(len(a)):
    if b == a[i:len(b)+i]:
        count = count+1
print(count)
