words={'사과':'apple','책상':'desk','학교':'school'}

for i in words:
    answer=input("{}에 해당되는 영어 단어를 입력해주세요: ".format(i))
    if(words[i]==answer):
        print("정답입니다!")
    else:
        print("틀렸습니다!")
