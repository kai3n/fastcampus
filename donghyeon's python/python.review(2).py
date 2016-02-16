"""파이썬의 비교연산자
== : 같다     != : 다르다        < : 보다작다        <= : 보다작거나 크다       > : 보다크다
>= : 보다크거나 같다       in : 멤버쉽

True 와 False 값 구분하기  대체적으로 1이면 True 이고 0이면 False 인데 예외로 아래 요소들은 모두다 False값을 같는다
null = None, 정수 0 = 0, 부동소수점수 0 = 0.0, 빈 문자열 = '', 빈 리스트 = [], 빈 튜플 = (), 빈 딕셔너리 = {}, 빈 셋 = set()

                                                                                                                """

"""
비교구문   1-1
         1.값이 무조건 boolean 값이여야하고 0,1 이여야한다.
         2. 조건 테스트 안에서 조건 테스트를 또 할 수 있다.
         3. 두개이상의 조건 테스트가 있다면 elif를 사용할 수 있다.
         4. 예외로 False 값 같은 것들 테스트해보기
                                                                                                            """

print('-----1-1-1-----------')
disaster = True
if disaster:
    print("Woe")
else:
    print('Whee')

print('------1-1-2----------')
furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear.")
else:
    if small:
        print("It's a skink")
    else:
        print("It's a human, Or a hairless bear.")

print('------1-1-3----------')
color = "puce"
if color =="red":
    print("It's tamato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee perple":
    print("I'don't know what it is, but only bees can see it")
else:
    print("I've never heard about"+color)

print('-------1-1-4-----------')
some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey,it's empty!")



"""While   2번
        ===========루프!!!
         한번이상 반복적으로 실행하기 위해선 루프! 가 필요하다.
         파이썬에서 가장 간단판 루핑 매커니즘은 while 문 이다.
                                                        """
print('--------2---------')
count_1 = 1                   # 카운트 = 1
while count_1 <= 5:           # 카운트 1이 성립됨            카운트가 2가됨 즉 성립함   ...   카운트6이됨 하지만성립안함
    print(count_1)            # 현재 카운트 1이프린트됨        2 프린트함           ...     프린트안함 와일문 멈춤
    count_1 += 1              # 카운트가 2개됨              카운트가 3이됨         ...

"""      2-1
어떤 일이 일어날 때까지 반복하고 싶지만, 어떤 일이 언제 일어날지 확실하지 않다면 무한루프 속에 break문을 사용하자
                                                                                        """
print('------2-1--------')
while True:                                                    # while 이 True 일때
    stuff = input("String to capitalize[tpye q to quit]:")     # 스터프라는게 문자열을 콘솔창(input())에 나타내는거임
    if stuff == 'q':                                           #근데 q를 콘솔창에 치면 와일문이 브래이크됨
        break
    print(stuff.capitalize())                                  #칠때 앞글자가 대문자로 바뀌게 프린트해주란뜻

"""    2-2
위처럼 반복문을 중단하고 싶지는 않지만 몇몇 이유로 다음 루프로 건너뛰고 싶을때가있다. 이럴때 continue를 사용한다 """

print('-----2-2---------')
while True:                                                 #while이 True 일때
    value = input("Integer,please[q to quit]:")             #콜솔창에 "" 실행하는것이 value다 명시
    if value =='q': #quit                                   #만약 value에 문자열q를 넣었을때
        break                                               # 브레이크한다
    number = int(value)                                     #number은 value 즉 콜솔창에 "" 실행하는에 숫자를 친다는소리
    if number % 2 == 0: # an even number                    #만약 bumber에 짝수를 친다면 %2는 나머지가 0이란소리 그럼 짝수
        continue                                            #짝수를친다면 계속된다

    print(number,"squared is", number*number)             # 홀수를 치면 홀수 " 문자열" 그홀수 *홀수 가 프린트됨
                                                            #짝수는 그냥 지나가고 q를 입력하면 끝남

"""   2-3
        Break는 어떤것을 체크하여 그것을 발견했을 경우 종료하는 while문을 작성할 때 사용한다
        While문이 모두 실행되었지만 발견하지 못했을 경우에는 else가 실행된다                 *  a = a+1
                                                                               = a += 1
                                                                                        """
print('----------2-3----------')
numbers = [1,3,5]                                 #numbers 는 리스트
position = 0                                      # position은 0
while position < len(numbers):                    # 포지션이 넘버스의 길이 즉 3보다 같거나 커지면 루프 정지
    number = numbers[position]                    # 넘버는 넘버스의 인덱스값
    if number % 2 ==0:                            # 만약 넘버스의 인덱스값이 짝수면
        print('Found even number', number)        # 짝수를 찾았다는 문자열과 넘버를 프린트해줌
        break                                     # 그리고 멈춤
    position += 1                                 # 한번 루프가 된후 포지션을 +1 해줌
else: # break not called                          # 만약 넘버가 짝수가아니면
        print('No even number found')             # 짝수를 못찾았다는 문자열을 프린트해줌

"""   3번
    반복문 for : 파이선에서 이터레이터는 자주 유용하게 쓰인다. 자료구조가 얼마나 큰지 어떻게 구현되었는지에 관계없이
    자료구조를 순회할 수 있도록 해준다.
                                                                                        """

""" 3-1
    우선 while을 써서 그문장을 for문으로 순회햇을때 더간결진 코드로 볼수있다.
                                                                    """
print('----3-1--------')
rabbits = ['Flopsy','Mopsy','Cottontail','Peter']
current = 0
while current < len(rabbits):    #          0 < 4      1 < 4              2 < 4           3 < 4
    print(rabbits[current])  #        래빗츠의0번쨰인덱스 레빗츠의 1번째인덱스 레빗츠에 2번째인덱스 레빗츠의 3번째인댁스 프린트
    current += 1             #                0           1                 2                3
## 이것을 for 문으로 바꾸면
print('----3-1-cf------')
for rabbit in rabbits:
    print(rabbit)

""" 3-2
    튜플이나 리스트는 한번에 한 항목을 순회한다. 문자열은 다음과 같이 한번에 한문자를 순회한다.
                                                                                    """
print('-------3-2------')
word = 'cat'                # len(cat) =3  길이 하나씩 가져옴
for letter in word:
    print(letter)

""" 3-3
        1. 딕셔너리의 순회는 키를 반환한다.
        2. 딕셔너리에서 키보다 값을 순회하려면 딕셔너리의 values()함수를 사용한다.
        3. 튜플에서 키와 값을 모두 반환하기 위에서는 items()함수를 사용한다
        4. 한번에 튜플 하나씩 할당 할 수 도있다.
                                                                    """

accusation = {'room':'ballroom','weapon':'lead pipe','person':'Clo. Mustard'}
print('-----3-3-1---------')
for card in accusation: #또는 accusation.keys():              # 키값만 카드에 하나씩 넣은 후
    print(card)                                              # 프린트함

print('-----3-3-2---------')
for value in accusation.values():                           #value만 밸류에 하나씩 넣은후
    print(value)                                            # 프린트함

print('-----3-3-3----------')
for item in accusation.items():                             #왜 튜플인거지 ?                                      승권형찬스
    print(item)

print('-----3-3-4----------')
for card, contents in accusation.items():
    print('Card',card,"has the contents",contents)

""" 3-4
    zip() 함수를 사용해서 여러 시퀀스를 병렬로 순회해보자  엄청난 순회방법이다.!!
    특징 ! 여러 시퀀스중 가장 짧은 시퀀스가 완료되면 zip()은 멈춘다
                                                                                                    """
days = ['MON','TUE','WEN']
fruits = ['banana','orange','peach']
drinks = ['coffee','tea','beer']
desserts = ['tiramisu','ice cream','pie','pudding']

print('------3-4-------')
for day,fruit,drink,dessert, in zip(days,fruits,drinks,desserts):
    print(day,":drink", drink,"-eat", fruit,"-enjoy",dessert)
print('----zip()---------')
#### zip()을 사용하여 영어와 한국어 단어에 대응하는 두개의 튜플을 만들어보세
english = 'MON','TUE','WED'
korean = '월','화','수'
print(list(zip(english,korean)))

#zip()의 결과를 다시 dict()에넣어보자
print(dict(zip(english,korean)))


""" 3-5
    range() 함수는 리스트나 튜플같은 자료구조를 생성하여 저장하지 않더라도 특정 범위 내에서 숫자스트림을 반환한다.
     range(start,stop,step)형식을 사용한다 만약 start를 생략하면 범위는 0에서 시작한다
     Stop은 꼭 입력해야 하는 값이다 step의 기본값은 1이다.
                                                                                                """
print('------3-5------------')
for x in range(0,3):             # x에 0 들어가고 1 , 2, 가들어감
    print(x)                     # 0 , 1, 2, 프린트됨
print(list(range(0,3)))

print('------3-5-1---------')
#거꾸로 진행하는 2에서 0의 숫자 시퀀스를 만들어보자
for x in range(2,-1,-1):         # x에 2 , 1, 0 까지들어감  - 스텝으로 #만약 스텝이 플러스면 값이 안나오겟지
    print(x)
print(list(range(2,-1,-1)))
print('------3-5-2---------')
# 0에서 10까지 2칸씩 진행하는 짝수 리스트를 만들어보자
print(list(range(0,11,2)))



"""
    컴프리헨션 !!!