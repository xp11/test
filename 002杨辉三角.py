curl=[1]
print(curl)
for i in range(1,7):
    for j in range(1,i):
        curl.append(pre[j-1]+pre[j])
    curl.append(1)
    pre=curl.copy()
    print(pre)