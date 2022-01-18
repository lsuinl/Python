result=0
i=0
suin=[]
while (1):
    suin.append(input("성적을 입력하세요(종료 시-1 입력):"))
    if(suin[i] == "-1"):
        break
    i+=1
    
for i in range(len(suin)):
    result+=int(suin[i])

print("합계: {}, 평균: {}".format(result,result/i))
