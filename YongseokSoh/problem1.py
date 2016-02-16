# [문제]
# 공대생 박민건은 교내 공모전에 출품하기 위해서 문자열 압축 알고리즘을 개
# 발하고 이를 민건 압축알고리즘을 뜻하는 MCA로 부르기로 했다. MCA는 연속
# 된 동일한 문자들을 해당 문자 하나와 그 문자가 연속된 수로 변환하여 압축
# 한다. 예를 들어, 문자열 “xxxwbbwww”가 주어졌을 때, 이는 “x3wb2w3”으
# 로 압축된다. (연속된 문자의 수가 1일 때는 압축하지 않는다.) 만약 연속된
# 문자의 수가 9를 넘어갈 경우에는 9개까지만 압축하고 새롭게 문자열 압축
# 을 한다. 예를 들어, 문자열 “xxxxxxxxxxxx”는 x12가 아닌 x9x3으로 압축
# 된다. 압축된 문자열의 길이를 t, 원본 문자열의 길이를 s라고 했을 때, 압축
# 률은 r= t/s와 같다. MCA의 성능을 평가하기 위하여 문자열이 주어졌을 때 각
# 문자열의 압축률 r을 구하는 프로그램을 작성하시오.
#
# 입력형식:
# 입력은 standard in첫 번째 줄에 테스트 케이스의 개수 m이 주어진다. 두 번째 줄부터 번째 줄에는 각 테스트 케이스의 문자열이
# 주어진다. 입력받은 각 문자열의 길이는 최대 10,000이다.
#
# 출력형식:
# 출력은 standard out으로 표시하며, 각 테스트 케이스별로 압축률 r을 출력
# 한다. 압축률은 반올림하여 소수점 3째 자리까지 출력한다.
#
# 예
# 입력
# 4
# x
# xxxwbbwww
# xxxxxxxxxxxx
# xxwbwxbwwwxwxwwwbbwxxwbbwwbxbwwwb
# 출력
# 1.000
# 0.778
# 0.333
# 0.909

string = "gkkkkttttttttttttbbbblllllllllllllpppppppppppppppggggggdddiyyyyyyggggggggggdddddxxxxxxxxxxxxxxxxff"

#string = "x"
#string = "xxxwbbwww"
#string = "xxxxxxxxxxxx"
#string = "xxwbwxbwwwxwxwwwbbwxxwbbwwbxbwwwb"
# 출
#1.000
#0.778
#0.333
#0.909

def mca_algorithm(string):
    mca = '' # to store answer
    cnt = 1 # if exceeds 9 times
    buf = '' # to remember element before
    for e in string:
        if e is buf:
            if cnt is 9:
                mca+=str(cnt)
                mca+=e
                cnt = 1
            else:
                cnt += 1

        else: # 앞의 글자랑 매칭이 안될때
            if cnt >1 : # several sequences
                mca+=str(cnt)
                mca+=e
                cnt = 1
            else:
                mca+= e
        buf = e

    if cnt >1:
        mca+=str(cnt)

    return mca

def compress_ratio(string):
    org = len(string)
    compressed = len(mca_algorithm(string))

    return round(float(compressed/org), 3)

print(string)
print(mca_algorithm(string))
print(compress_ratio(string))