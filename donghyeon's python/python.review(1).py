'''파이썬 정리 파일


 1 . 파이썬에서 변수 혹은 리터럴값의 타입을 알고싶다면 type()를 사용하면된다'''                                                #tpye()
a= 7
print('----1번----')
print(type(a))
print(type(58))
print(type(99.9))
print(type('abc'))

"""2 . 파이썬의 연산자 특징 알아보기"""                                                                              #연산자특징
print('----2번----')
print(5 + 8)            #덧셈 연산자
print(90 - 10)          #뺄셈 연산자
print(4 * 7)            #곱셈 연산자
print(7 / 2)            #나눗셈 연산자
print(7 // 2)           # 나눗셈을 한후 나머지값은 버린체 결과 나옴
print(7 % 3)            # 나눗셈을 한수 나머지의 결과값만 나옴
print(3 ** 4)          #3의 4제곱을 의미함

""" 3.  형변환  (다른데이터타입을 정수형으로 변환 시킬려면 int()함수를 사용한다 이함수는 소수점을 버리고 정수를 반환한다"""               #형변환
print("----3번------")
print(int(True))
print(int(False))
print(int(98.6))
print(int(1.0e4))
print(int(4+7.0))    #<< 숫자 타입을 적어도 자동으로 형변환!(파이썬의 위대함)
#부동소수점수로 형변환
print(float(True))
print(float(98))
print(float('1.0e4'))
#str() 를 이용하여 데이터타입을 문자열로 변환
print(str(102))
print(str(True))      # 여기서 boolean 값이랑 프린트된 True 값은 다르다
""" 4. 문자열 """                                                                                                #문자
#문자 앞에 백슬레시(\)기호를 붙임으로써 특별한 의미를 줄수있다.
palindrome = 'A man,\nA plan,\nA canal:\nPanama.' #\n 은 new line 이란소리로 프린트될때 다음줄로 옮겨진다.
print('---4번----')
print(palindrome)
# 4-1.  \t = tab
print('------4-1---')
print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')

#4-2. 결합하고 복제하기
print('Release the Kraken!' + 'At once@')   # 결합
start = "Na" * 4 + '\n'
middle = "Hey" * 3 + '\n'
end = 'Goodbye'
print('-------4-2-------')
print(start+start+middle+end)

#4-3. 문자 추출
letters = 'abcdefghijklnmopqrstuvwxyz'
print('------4-3------')
print(letters[0])   # [] 안에 보고 싶은 인덴트를 넣는다
print(letters[-2])
print(letters[25])
#4-4 슬라이스 (문자열에서 문자열 일부를 추출한다)
# [:] - 처음부터 끝까지 전체 시퀀스 추출
# [start:] - start 오프셋(자리)부터 끝까지 시퀀스를 추출
# [:end] - 처음부터 end-1 오프셋(자리) 까지 시퀀스 추출
# [start:end] - start 오프셋부터 end-1 오프셋 까지 시퀀스를 추출
# [start:end:step] - step 만큼 문자를 건너 뛰면서 start 오프셋부터 end-1 오프셋 까지 시퀀스 추출
print('--------4-4-------')
print(letters[:])
print(letters[20:])
print(letters[:20])
print(letters[-3:])
print(letters[::7])
print(letters[4:20:3])
print(letters[19::4])

#4-5 len() << 길이알려주는
print('------4-5-----')
print(len(letters),':'," 알파벳 a~z 몇개인지")

#4-6 문자열 결합하고 분리하는 join() , split() 함수
print('-------4-6---------')
crypto_list = ['Yetl', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ','.join(crypto_list)
print("Found and signing book deals:", crypto_string)

todos = 'get gloves, get mask, give cat vitamins,call ambulance'
print('------------------')
print(todos.split(',')), print('쉼표를 기준으로 분류함 ')
print(todos.split()), print('공백을 기준으로 분류함')

#4-7 문자열을 자유롭게 다뤄보자
# .startswith(' ') = ' '로 시작하는가
# .endswith(' ') = ' ' 로 끝나는가
# .find(' ') = ' ' 값이 첫번째로 나오는값 찾기
# .rfind(' ') = ' ' 마지막으로 나오는값 찾기
# .count(' ') = ' ' 몇번나오는가
# .isalbum() = ' ' 알파뱃과 숫자로만 이루어져있는가

poem = "All that doth flow we cannot liquid nameor else would fire " \
       "and water be the same; But that is liquid Which is moist and " \
       "wetFire that property can never get.Then 'tis not cold tha doth " \
       "the fire put outBut 'tis the wet that makes it die, no doubt.'"
print('-----------4-7------------')
#처음 13자 출력
print(poem[:13])
# 이시는 몇글자로 되있는가?
print(len(poem))
#이시는 All 로 시작하는가 ?
print(poem.startswith('All'))
#이시는 That's all,folks! 로 끝나는가?
print(poem.endswith("That's all,folks!"))
#이시에서 첫번째로 the 가 나오는 오프셋은?
print(poem.find("the"))
#이시에서 마지막으로 the 가 나오는 오프셋은?
print(poem.rfind("the"))
#세글자 the 가 몇번 나오는가 ?
print(poem.count("the"))
# 이시는 글자와 숫자로만 이루어져 있는가?
print(poem.isalnum())

#4-8
# .strip('.')       마침표 제거 앞과 끝에서부터 찾는다 바로 못찾으면 실행안됨
# .capitalize()    앞에있는거 대문자 바꾸기
# .title()         모든단어 첫글자 대문자로바꾸기
# .upper()          전체 대문자
# .lower()          전체 소문자
# .replace('a','b')    기존에 있던 a를  b로 바꿈
setup = 'a duck goes into a bar...'
print('------4-8------')
#','들 제거 해보기
print(setup.strip('.'))
print(setup.strip('into'))    #사이에 낀 into 를 찾을수없는걸로봐서 바로앞과 뒤의 위치만 성립되는듯
# 첫단어를 대문자로 만들기
print(setup.capitalize())
# 모든단어의 첫글자를 다 대문자로
print(setup.title())
# 글자를 모두 대문자로
print(setup.upper())
# 글자를 모두 소문자로
print(setup.lower())
# duck 를 marmoset 으로 바꾸기
print(setup.replace('duck','marmoset'))

"""5 파이썬에서는 두가지 다른 시퀀스(순서되로 저장되는) 구조가 있다. 튜플과 리스트이다. 파이썬은 왜 이두가지를                   #리스트
모두 포함하고 있을까?
 튜플은 불변한다. 즉 튜플에 항목을 할당하고 이를 바꿀수 없다. - 활용 :절대바뀌면안되는값을 만들때
 리스트는 항목을 할당하고 자유롭게 수정하거나 삭제할 수 있다.

우선 리스트부터
"""

#5리스트 : 항목할당후 자유롭게 수정, 리스트는 데이터를 순차적으로 파악하는데 유용하다. 특히 데이터의 순서가 바뀔수 있다는
#점에서 유용하다. 리스트를 묶을땐 [ ] <<사용한다

empty_list = []
weekdays = ['MON','TUE','WED','THU','FRI']
big_birds = ['emu','ostrich','cassowary']
first_name = ['graham','john','terry','Michael']
another_empty_list = list()
print('----------5------------')
print(empty_list)
print(weekdays)
print(big_birds)
print(first_name)
print(another_empty_list)

# 5-1 데이터 타입>> 리스트
# 5-2 튜플 >> 리스트
# 5-3 split()으로나뉜 문자열 >> 리스트
print('---------5-1------')
print(list('cat'))

print('---------5-2------')
a_tuple = ('ready','fire','aim')
print(list(a_tuple))

print('---------5-3------')
birth_day = '9/1/1993'
print(birth_day.split('/'))    #split() 자체가 리스트를 만들어주는거같음.
# 5-4 리스트는 오프셋 으로 하나의 특정값을 추출할수 있다 .
# A=[오프셋넘버]
print('---------5-4------')
marxes = ['groucho','Chico', 'Harpo']  # 인덱스 1,2,3 이아니라 0, 1, 2  이런식
print(marxes[2])
print(marxes[-1])
print(marxes[1])

'''5-5
리스트는 다음과 같이 리스트 뿐만아니라 다른타입의 요소도 포함할 수 있다. (리스트 안에 리스트 중복가능)
그리고 인덱스 추출시 name_of_list[index_1][index_2] 이런식                               '''

print('---------5-5------')
small_birds = ['hummingbird','finch']
extinct_birds = ['dodo','passenger pigeon','Norwegian Blue']
carol_birds = [3,'French hens','2','turtledoves']


all_birds = [small_birds, extinct_birds, 'rmacaw', carol_birds]
print(all_birds)
print(all_birds[1][0])     #dodo      >> 두인덱스 사용해서 추출하기 .

""" 5-6
오프셋으로 항목을 얻어서 바꿀수있다.
슬라이스로 항목 추출하기
append()함수를 사용하여 리스트의 끝에 항목추가하기                  """

print('---------5-6------')
marxes = ['Groucho','Chico','Harpo']
marxes[2] = 'Wanda'                       #marxes 리스트의 2번째 인덱스자리에오는 항목을 'wanda'로 바꿈
print(marxes)

print(marxes[0:2]) # 슬라이스로 이범위내에있는 항목만 추출하기

marxes.append('Zeppo')   #가장자리에 'Zeppo' 추가하기
print(marxes)
""" 5-7
Extend() 를 사용하여 다른리스트를 병합해보자
+= 로도 병합할수있다.
append() 를 사용하면 항목을 병합하지않고 리스트 전체가 추가된다.
**extend() 와 append() 가 각각 어떤결과를 추출하는지 확인하자**
insert() 로 항목추가하기                                """

print('---------5-7------')
marxes = ['Groucho','Chico','Harpo','Zeppo']
others = ['Gummo','Karl']
marxes.extend(others)
print(marxes)


print('--------cf------')
marxes = ['Groucho','Chico','Harpo','Zeppo']
others = ['Gummo','Karl']
marxes += others
print(marxes)

print('------cf_1-----')
marxes = ['Groucho','Chico','Harpo','Zeppo']
others = ['Gummo','Karl']
marxes.append(others)
print(marxes)

print('------cf_2-----')
marxes = ['Groucho','Chico','Harpo','Zeppo']
marxes.insert(3,'Gummo')                         # insert(위치,추가할항목)
print(marxes)

print('------cf_3-----')
# cf_1 에서 리스트 안에있는 리스트에 항목추가하기
marxes =['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'Karl']]
marxes[4].insert(1,'개새')
print(marxes)
""" 5-8
오프셋으로 항목삭제하기 del name_of_list[index]
삭제할 항목의 인덱스를 모를때 remove(" ")
항목을 가져오는 동시에 그항목을 삭제하는 pop()                   """

print('---------5-8------')
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']
del marxes[-1]
print(marxes)

print('------cf-1-------')
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']
marxes.remove("Karl")
print(marxes)
print('-----cf-2----------')
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']
print(marxes.pop())       #항목을 가져오는 동시에 삭제함 ,  pop() 괄호안에 아무것도 없을땐 마지막항목을 가져오고 사라짐
print(marxes)

""" 5-9
항목값의 리스트 오프셋을 알고싶다면 index()를 사용하면된다.
리스트에 어떤값의 존재를 확인할려면 in 을 사용하면된다
리스트에서 값이 적어도 하나이면 존재하면 in 은 true 를 반환한다.  즉(같은값이 2개 이상있어도 Ture 를 반환함
리스트에서 항목수를 알고 싶다면 len() 함수를쓰자            """

print('---------5-9------')
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo','Zeppo']

print(marxes.index('Chico'),':'," 인덱스넘버")   #인덱스 확인

print('Groucho' in marxes)                       # 존재여부확인

print('BoB' in marxes)

print('Zeppo' in marxes)            # 동일한 항목이 2개이상이여도 True 를 반환함

print(len(marxes))
""" 5-10
sort  와 sorted 의 차이
기본적으로 두기능은 리스트 자체를 내부적인 순서(숫자: 오름차순 , 문자 : 알파벳순 )에의해  정렬해준다
sort : 기존의 리스트 값 즉 순서가 바뀜    [[  name_of_list.sort()  ]]
sorted  기존에 있던 순서는 안바뀜 즉 정렬된 복사본을 반환함 [[  list_copied = sorted(name_of_list
                                                                                     """
print('---------5-10------')
A = ['b','c','a']
A.sort()
print(A)

print('------cf_1----')
A = ['b','c','a']
B = sorted(A)
print(B)
print(A)

""" 5-11  b = a 의 관계에대해
          완전히 새로운 리스트로 복사하고싶으면      name_of_list.copy()  ,    new_list = list(name_of_list)
                                                                                           """

print('----------5-11------')
a = [1,2,3]
b = a                       # a 를 비에 넣는다는 뜻임, 데이터를 넣었을때 같은 메모리상에 저장됨
print(b)
a[0] = 'surprise'
print(a)                    # 그결과로 a 의 값도 변경됨
print(b)

"""5-12
       copy() 함수
       list() 변환 함수
       슬라이드 [:]
                            """
print('--------5-12-----')
a = [1,2,3]
b = a.copy()                       #name_of_list.copy()
c = list(a)                        # list(name_of_list)
d = a[:]
a[0] = 'integer lists are boring'
print(a)                           # b,c,d 값은 디폴트를 유지한다.
print(b)
print(c)
print(d)

""" 6_1 , 6_2, 6_3 6_4                                                                                   튜플
       튜플!!  임의적인 항목의 시퀀스, 리스트와 다르게 튜플은 불변한다. 즉 튜플을 정의한후에는
       추가, 삭제, 수정을 할수없다는 것을 의미한다.그러므로 튜플은 상수의 리스트라고 할수있다.
       -튜플생성
       -튜플언패킹
       -값교환 튜플
       -다른객체를 튜플로 만들기
                                                                                  """
print('------6-1-----')
empty_tuple = ()
print(empty_tuple)

print('------cf_1----')
one_marx = 'Groucho'
one_marx_tuple = 'Groucho',               # 하나 이상의 요소가 있는 튜플을 만들기 위해서는 각 요소 뒤에 콤마(,)를 붙인다.
print(one_marx)                           # 한개만 있을때는 뒤에 , 가있다는게 튜플
print(one_marx_tuple)

print('------cf_2-----')
marx_tuple = 'Groucho','Chico','Harpo'    #두개 이상의 요소가 있을경우, 마지막 요소에는 콤마를 붙이지 않는다.
print(marx_tuple)
marx_tuple = ('Groucho','Chico','Harpo')  #파이썬은 튜플을 출력할때 괄호를 포함한다.
print(marx_tuple)

print('-------6_2----')
marx_tuple = ('Groucho','Chico','Harpo')
a,b,c = marx_tuple                        # 튜플은 한 번에 여러 변수를 할당할 수 있다. -튜플 언패킹-
print(a)
print(b)
print(c)

print('------6_3-----')
password = '1234567810'
icecream = 'tuttifrutti'
password,icecream = icecream,password     # 한문장에서 값을 교환하기위해 임시변수를 사용하지 않고 튜플을 사용할수있다.
print(password)
print(icecream)

A = [1]                                   #리스트도되네 ?
B = [2]
A,B=B,A
print(A , '리스트 값변경')
print(B , "리스트 값변경")

print('------6_4-----')
marx_list = ['Groucho','Chico','Harpo']   #list>>tuple  tulpe() 은 다른객체를 튜플로 만들어준다.
tuple(marx_list)

""" 튜플과 리스트
       리스트를 대신해서 튜플을 사용할 수가 있다. 하지만 튜플은 리스트의 append(),insert()등과 같은 함수가없고
       함수의 수가 매우 적다. 튜플을 생성한 후에는 수정할 수가 없기 때문이다  그러면 리스트를 사용하면 되지,
       왜튜플을 사용할까?
       - 튜플은 더 적은 공간을 사용한다
       - 실수로 튜플 항목이 손상될 염려가 없다.
       - 튜플은 딕셔너리 키로 사용할수있다.
       - Named tuple 은 객체의 단순한 대안이 될 수 있다.
       - 함수의 인자들은 튜플로 전달된다 .****      #근데 일반적으로 리스트와 딕셔너리를 많이씀
                                                                                    """

"""딕셔너리
       딕셔너리는 리스트와 비슷하다. 다른 점은 항목의 순서를 따지지 않으며 (there is no index) 0또는 1과같은 오프셋으로 항목
       을선택할 수 없다. 대신 값에 상응하는 고유한 키(보통은 문자열)를 저장한다. 이키는 대부분 문자열이지만,
       불변하는 파이썬의 어떤 타입이 될수있다. 딕셔너리는 변경 가능하므로 키-값 요소를 추가, 삭제, 수정 할수있다.
       다른 언어에서는 딕셔너리를 연관 배열 해시 해시맵 이라고 부른다
                                                                                                  """
""" 7-1 7-2
       딕셔너리 생성하기
       딕셔너리 변환하기

                                          """
print('---------7-1------')
empty_dict = {}
print(empty_dict)

bierce = {
"day" : "A period of twenty-four hours, mostly misspent",
"positive" : "Mistaken at the top of one's voice",
"misfortune" : "The kind of fortune that never misses",
}
print(bierce)

print('-------7-2------')
                                          # dict() < 사용 = 딕셔너리로 변환
lol = [['a','b'],['c','d'],['e','f']]       #리스트로된 리스트
lot = [('a','b'),('c','d'),('e','f')]       #튜플로된 리스트
tol = (['a','b'],['c','d'],['e','f'])       #리스트로된 튜플
los = ['ab','cd','ef']                      #문자열로된 리스트
tos = ('ab','cd','ef')                      #문자열로된 튜플

print(lol)
print(lot)
print(tol)
print(los)
print(tos)

print(dict(lol))
print(dict(lot))
print(dict(tol))
print(dict(los))
print(dict(tos))

"""7-3 7-4                                                                                             딕셔너리
       딕셔너리에 항목추가하기
       딕셔너리에 항목을 추가하는 것은 간단하다. 키에 의해 참조되는 항목에 값을 할당하면 된다.
       키가 이미 있는 경우는 그값은 새값으로 대체된다.
       -항목추가
       -update() 함수와 비교해보기
                                                                                    """

print('----------7-3-------')
pythons = {
       'Chapman' : 'Graham',
       'Cleese' : 'John',
       'Idle' : 'Eric',
       'Jones' : 'Terry',
       'Palin' : 'Michael',
}

print(pythons)
print('------------------------------------------------------------------------------------------------------------')
pythons["Gilliam"] = "Gerry"              #값변경 name_of_dict['key'] = 'value'
print(pythons)
print('------------------------------------------------------------------------------------------------------------')
pythons["Gilliam"] = "Terry"              #딕셔너리의 키들은 반드시 유일해야함, 만약 같은 키를 두번 이상 사용하면 마지막 값이 덮어씀
print(pythons)

print('---------7-4---------')
pythons = {
       'Chapman' : 'Graham',
       'Cleese' : 'John',
       'Giliam' : 'Terry',
       'Idle' : 'Eric',
       'Jones' : 'Terry',
       'Palin' : 'Michael',
}
print(pythons)
print('-----------------------')
others= {'Marx':'Groucho','Howard':'Moe'}
pythons.update(others)             #name_of_dict.update(new_dict)
print(pythons)                     #다른 딕셔너리를 결합할때 사용함


""" 7-5
       1.키와 del로 항목삭제하기.       del name_of_dict['key']
       2.모든 항목삭제하기.            name_of_dict()
       3.in 으로 키멤버십 테스트하기    'key' in name_of_dict
       4.에러 방지를 위해 in 을 사용하자
       (A['key'] 도키를찾을수있지만 만약 키가없으면 traceback 오류가남
       그래서 왼만하면 in을 써서 에러를 방지하자.
       5. get() 함수 사용하는방법   키가 존재하지 않을때 옵션 값을 지정해서 이를 출력한다.
                                                                             """
print('-----------7-5-1---------')
del pythons['Marx']
print(pythons)                     #'Marx'와 그의 value 값 삭제하기

del pythons['Howard']
print(pythons)

print('---------7-5-2-----------')
pythons.clear()                    # 모든항목삭제 A.clear()
print(pythons)

print('--------7-5-3------------')
pythons = {'A':'a','B':'b','C':'c'}
print('A' in pythons)                     #'key' in A
print('B' in pythons)                     #결과는 True
print('c' in pythons)                     #     False

print('-----------7-5-4----------')
print(pythons['A'])
#print(pythons['Z']) << 딕셔너리에 키가 존재하지 않으면 에러가남 !!!
#이러한 애러를 방지하기위해 in 으로 키에 대한 멤버십 테스트를 하는방법이다.
print('---------7-5-5-------------')
print(pythons.get('B'))
print(pythons.get('Z','Not a python')) # 만약 키가 딕셔너리에 없을떄 오류가안나고 옵션값을 호출함
print(pythons.get('Z'))    # 옵션 값을 지정하지않으면 None을 얻음

"""    7-6
       1. 모든 키 가져오기 name_of_dict.key()
       2. 모든 값 가져오기 name_of_dict.value()
       3. 모든 쌍의 키와값 가져오기 name_of_dict.items()
                                                                             """

signals = {'green':'go','yellow':'go faster','red':'stop'}
print('-------7-6-1--------')
print(signals.keys())
print(list(signals.keys()))  #딕셔너리를 리스트로 변환하기위해
print('-------7-6-2--------')
print(list(signals.values()))
print('-------7-6-3--------')
print(list(signals.items()))

"""셋  셋은 값을 버리고 키만 남은 딕셔너리라고 생각하면된다. 딕셔너리와 마찬가지로 각 키는 유일해야한다. 어떤 것이                        셋
   존재하는지 여부만 판단하기 위해서는 셋을사용한다 그리고 여기에 어떤 정보를 첨부해서 그 결과를 얻고 싶으면 딕셔너리를
   사용한다.
"""
""" 8-1
셋을 생성할떄는 set()함수 혹은 {}안에 콥마로 구분된 하나 이상의 값을 넣으면된다.
                                                                      """
print('--------8-1-----------')
empty_set = set()
print(empty_set)
print('---------')
even_number = {0,2,4,6,8}      # 딕셔너리 키와 마찬가지로 셋은 순서가 없다.
print(even_number)
print('---------')
print(set('letter'))         #중복된 값을 버린 셋을 생성한다    [[ set()  ]]

""" 8-2
        1. 리스트 >> 셋으로
        2. 튜플을 셋으로
        3. 딕셔너리 >> 셋으로     (딕셔너리에 set()을 사용하면 키만 사용한다)
        set( ('string') )
           (   (list)   )
           (   (tuple)  )
           ({'a:b','c:d'})
                                                                      """

print('-------8-2-1--------')
print(set(['Dasher','Dancer','Prancer','Mason-Dixon']))
print('-------8-2-2--------')
print(set(("Ummagumma","Echoes","Atom Heart Mother")))
print('-------8-2-3--------')
print(set({"apple":"red","orange":"orange","cherry":"red"}))   # 키값만 호출

""" 8-3                                                                                                      셋연산
       셋연산
       1. & 연산자와 intersection() 함수          &:교집합 a&b = a.intersection(b)
       2. | 연산자와 union() 함수                 |:합집합 a|b = a.union(b)
       3. - 연산자와 difference() 함수            - : 차집합 a-b = a.different(b)
       4. ^ 연산자와 symmetric_difference() 함수  ^ : 대칭차집합(교집합을제외한나머지) a^b = a.symmetric_difference(b)
       5.<= 연산자와 issubset()함수              <= : a셋이 b셋의 부분집합 a<=b = a.issubset(b)
                                                                                                  """

print('--------8-3-1------------')
a = {1,2}
b = {2,3}
print(a&b)
print(a.intersection(b))
print('--------8-3-2-------------')
print(a|b)
print(a.union(b))
print('--------8-3-3-------------')
print(a-b)
print(a.difference(b))
print('------8-3-4--------------')
print(a^b)
print(a.symmetric_difference(b))
print('-------8-3-5-------------')
print(a <= b)
print(a.issubset(b))
A ={2,3}
B ={2,3,4,5}
print('---8-3-5(cf)')
print(A <= b)
print(A.issubset(B))