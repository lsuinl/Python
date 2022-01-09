
name=input("이름을 입력하세요: ")
present=int(input("현재년을 입력하세요: "))
birth=int(input("탄생년을 입력하세요: "))
age=present- birth + 1

print("{}님의 나이는 {}세 입니다!".format(name, age))
