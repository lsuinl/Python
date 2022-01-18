a=[1,2,3,4,5]
b=[1,3,3,4,5,6,7]
i=0
c=[]

for i in range(len(a)):
    for j in range(len(b)):
        if(a[i]==b[j]):
            c.append(b[j])
c=list(set(c)) 

print("결과",c)
    
