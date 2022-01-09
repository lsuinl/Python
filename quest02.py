price=int(input("책 값을 입력하세요: "))
gkfdls=int(input("할인율을 입력하세요(%): "))
qothdfy=int(input("배송료를 입력하세요: "))
gkq=price-(price*gkfdls/100)+qothdfy
print("결제 금액: {}원".format(int(gkq)))
