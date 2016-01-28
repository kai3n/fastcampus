def hanoi_tower(num):
    if num is 1:
        return 1
    else:
        return 2*hanoi_tower(num-1)+1

print(hanoi_tower(3))
print(hanoi_tower(2))
print(hanoi_tower(10))

def hanoi_instruction(num, startPeg=1, endPeg=3):
    if num:
        hanoi_instruction(num-1,startPeg,6-startPeg-endPeg)
        print("{}번 디스크를 {}번 막대에서 {}번 폴대로 이동시키시오.".format(num, startPeg, endPeg))
        hanoi_instruction(num-1,6-startPeg-endPeg,endPeg)

hanoi_instruction(3)

"""
하노이강의 있음
열혈강의 자료구조 강의 쿠폰 등록해놨습니다. 로그인 하시면 들으실 수 있어요.
아이디는 fastcampus 이고 비밀번호는 자료구조 입니다.
 영타로 자료구조 라고 쓰시면 됩니다.
 책도 필요하신 분 있음 가져갈게요. 공공재로 씁시다. 어차피 사놓고 1년 동안 들여다 보지도 않았네요ㅋㅋ
 http://www.orentec.co.kr/teachlist/DA_ST_1/teach_sub1.php
"""