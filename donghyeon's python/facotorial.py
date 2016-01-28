"""
재귀 하수의 몸체안에서 함수를 한번더 호출하는



1ㅡ>2ㅡ>3ㅡ>4                                                      factorial(0) = 1
A->Bㅡ>C-->D       :제일 먼저 호출되는 함수가 제일 마지막에 종료됨           factorial(1) = 1
4<-3<-2<--1

f(n) = n x f(n-1) .. .. .. n>=1 재귀대명사의 포인트


"""

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
