maxx=-10000000000
data=[-12,3,-9,5,8,-2,0,-8,3,10]
avg=0
count=0


for i in range(len(data)):
    if(maxx<data[i]):
        maxx=data[i]

print("가장 큰 수: {}".format(maxx))

while (count!=10):
    if((count+1)%2==0):
        avg+=data[count]
    count+=1

 

print("합계: {}, 평균: {}".format(avg, avg/(len(data)-5)))


data.sort(reverse=True)
print(data)
