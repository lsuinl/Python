suin=[]
for i in range(1,100):
    num=i
    for j in range(2,i):
        if i%j==0:
            num=j
            break
    if num==i:
        suin.append(i)

print(suin)
