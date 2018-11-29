import math
a=[2]
for i in range(2,101):
    for j in a:
        if i%j==0:
            break
        if j > int(math.sqrt(i)):
            a.append(i)
            break
print(a)