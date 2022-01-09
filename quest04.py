pyear=int(input("현재년을 입력해 주세요:"))
pmonth=int(input("현재월을 입력해 주세요:"))
pday=int(input("현재일을 입력해 주세요:"))
year=int(input("출생년을 입력해 주세요:"))
month=int(input("출생월을 입력해 주세요:"))
day=int(input("출생일을 입력해 주세요:"))
print("-----------------------------------------------------------")
print("오늘 날짜: {}년 {}월 {}일".format(pyear,pmonth,pday))
print("생년 월일: {}년 {}월 {}일".format(year,month,day))
print("-----------------------------------------------------------")
if(pmonth==month and pday>=day):
    aks=pyear-year-1
elif(pmonth>month):
    aks=pyear-year-1
else:
    aks=pyear-year-2
print("만 나이: {}세".format(aks))
print("-----------------------------------------------------------")
