num=[23,4,2,5,6,34]

'''suin=[]

def wow(x):
     for i in x:
        if (i%2==0):
            suin.append(i)
print(wow(num))
'''

suin=list(filter(lambda x: x % 2 == 0, num))
print(suin)
