user_info=('김수인','0403')

while (1):
    ide=input("관리자 아이디를 입력하세요: ")
    passward=input("관리자 비밀번호를 입력하세요: ")
    if(ide!=user_info[0] or passward!=user_info[1]):
        print("아이디 또는 비밀번호가 잘못 입력되었습니다.")
    else:
        print("본인 확인이 되었습니다.")
        break
