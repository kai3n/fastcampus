# '''
# sentence = "I am a boy"
#
# def word_count(sentence):
#     return len(sentence.split())
#
# print(word_count(sentence))
#
# #####################################################################################################################
# string1 = "I am a boy"
# string2 = ["I", "am", "a", "boy"]
# string3 = ("I", "am", "a", "boy")
# string4 = {"I" : "am", "a" : "boy"}
# string5 = [1,2,'abc',0.1,'efd']
#
# def search(input, word_or_character):
#     if type(input) == str:
#         if str(word_or_character) in input:
#             return True
#     elif type(input) == tuple or type(input) == list:
#         empty_string = ""
#         for element in input:
#             empty_string += str(element)
#         if word_or_character in empty_string:
#             return True
#     return False
#
# print(search(string5, "bc"))
#
# #####################################################################################################################
# def range_func(input, start, end, step):
#     index = start - 1
#     element_list = []
#
#     if start >= 0:
#         while index < end:
#             element_list.append(input[index])
#             index += step
#         return element_list
#
#     # Todo: backward range functino yet to be coded
#     else:
#         index = len(input) + start
#         while index < end:
#             element_list.append(input[index])
#             index += step
#         return element_list
#
# input = "123456789"
# print(range_func(input, -1, -5, -2))
#
# #####################################################################################################################
#
# def print_args(*args):
#     print("Positional argument tuple:", args)
#
# print_args("adfasdf","Asdfasdf","asdfasdfasdf")
#
# def print_kwargs(**kwargs):
#     print('Keyword arguements:',kwargs)
#
# print_kwargs(wine="merlot", entree='mutton', dessert='macaroon')
#
# #####################################################################################################################
#
# def answer():
#     print(42)
#
# answer()
#
# def run_something(func):
#     func()
#
# run_something(answer)
#
# ######################################################################################################################
# animal = "fruitbat"
#
# def change_and_print_global():
#     #global animal
#     animal = "wormbat"
#     print("inside chang_and_print_global:", animal)
#
# print(animal)
# change_and_print_global()
# print(animal)
#
# ######################################################################################################################
# #
# # 14일 목요일: 퀴즈 문제
# #
# def reverse_word(word):
#     if len(word)<=0:
#         print ("No word")  ####redundant & 프린트와 return None이 둘 다 반환 -> return "No word"로 두 줄을 한 줄로 줄일 수 있겠다
#         return None
#     else:
#         empty_word = ""
#         for char in word[::-1]:
#             empty_word += char
#         word = empty_word
#         return word
#
# print(reverse_word(""))
# '''
#
# ######################################################################################################################
# # 날짜: 2016.1.14
# # 과제: upper() & lower() 구현
# # 내용: upper()와 lower()는 string class의 method이다. 문자열 객체가 method를 호출하면, 각각 대문자와 소문자로 변환한다.
# #      파라미터가 string이 아닌 경우에는 attributeError가 발생한다. 정확한 구현을 위해서는 string class 구현과 try-catch 구문을 사용해야 한다.
#
# def change_to_upper(word):
#     #인자로 받는 word가 문자열인 경우에만 함수를 실행한다.
#     if type(word) != str:
#         return "올바른 입력값이 아닙니다."
#     #올바른 형태의 인자가 들어왔을 경우만 변환 진행한다.
#     else:
#         uppered_word = ""
#         for character in word:
#             #소문자는 ASCII 코드상 97-122에, 대문자는 65-90에 해당한다. 같은 글자의 소문자 - 대문자의 차이는 32이다.
#             #함수 ord()는 글자를 해당 ASCII코드 숫자로, chr()는 ASCII 코드를 글자로 변환한다.
#             ascii_char = ord(character)
#             if ascii_char >= 97 and ascii_char <= 122:
#                 character = chr(ascii_char - 32)
#             uppered_word += str(character)
#         return uppered_word
#
# #Change_to_upper()의 코드를 살짝 바꾸면 된다
# def change_to_lower(word):
#     if type(word) != str:
#         return "올바른 입력값이 아닙니다."
#     else:
#         lowered_word = ""
#         for character in word:
#             #소문자는 ASCII 코드상 97-122에, 대문자는 65-90에 해당한다. 같은 글자의 소문자 - 대문자의 차이는 32이다.
#             #함수 ord()는 글자를 해당 ASCII코드 숫자로, chr()는 ASCII 코드를 글자로 변환한다.
#             ascii_char = ord(character)
#             if ascii_char >= 65 and ascii_char <= 90:
#                 character = chr(ascii_char + 32)
#             lowered_word += str(character)
#         return lowered_word
#
# test_string1 = "abBzrTsdf134"
# test_string2 = 1234
#
# print(change_to_upper(test_string1))
# print(change_to_upper(test_string2))
# print(change_to_lower(test_string1))
# print(change_to_lower(test_string2))
#
# ######################################################################################################################
# '''
# def countdown(n):
#     print('counting down from %d' %n)
#     while n > 0:
#         yield n
#         n -= 1
#     return
#
# print(type(countdown))
# '''
# ######################################################################################################################
'''
import time

def elapsed_time(functor):
    def decorated(*args, **kwargs):
        start=time.time()
        functor(*args,**kwargs)
        end=time.time()
        print("Elapsed time:%f" % (end-start))
    return decorated

@elapsed_time
def hello():
    print("Hello")

hello()

print(locals())
print(globals())

# ######################################################################################################################

class Calculator():
    def __init__(self):
        pass
    def add(self, x, y):
        '두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return int(x + y)
    def subtract(self, x, y):
        '두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return float(x - y)
    def multiply(self, x, y):
        '두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return int(x * y)
    def divide(self, x, y):
        '두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'
        try:
            split_num = str(x/y).split(".")
            int_num = int(split_num[0])
            digit_to_compare = int(split_num[1][0])

            if int_num >= 0:
                if digit_to_compare >= 5:
                    return int_num + 1
                return int_num

            else:
                if digit_to_compare >= 5:
                    return int_num - 1
                return int_num

        except ZeroDivisionError: return "Division by zero."

    def expCalc(self,expStr):
        """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
        ex) expCalc('1+3-5')는 -1을 반환한다.
        ex) expCalc('1+3*5')는 20을 반환한다.
        ex) expCalc('1+3+5-0')는 9을 반환한다.
        ex) expCalc('4+3+5/3')는 4을 반환한다.
        """

        numbers = []        #숫자를 저장할 리스트
        operands=[]         #연산자를 저장할 리스트
        empty_string = ""   #숫자가 2자리 이상인 경우, numbers에 저장하기 전에 전처리

        for elem in expStr:

            #elem이 숫자인 경우, empty_string에 저장
            if elem.isdigit():
                empty_string += str(elem)
            #elem이 연산자인 경우, 그동안 받아들인 empty_string을 numbers에 저장후, elem은 operands에 저장
            #empty_string은 다시 초기화한다
            else:
                operands += str(elem)
                numbers.append(empty_string)
                empty_string = ""

        #마지막 숫자의 경우, append가 안되므로 예외처리
        numbers.append(empty_string)

        #총 연산의 횟수는 numbers에 저장된 숫자의 갯수-1이다.
        #앞에서부터 차근차근 계산을 해나간다.
        #eval()은 string을 계산처리해줌.
        for i in range(len(numbers)-1):
            result = str(numbers[i])
            temp = (eval(result + operands[i] + numbers[i+1]))
            result = temp

        print(result)




    def expCalcAdvanced(self,expStr):
        """숫자 표현식을 문자열로 받아서(이 때 *와 / 연산자는 우선순위로 계산함, ()괄호에 대한 우선순위도 매김)표현식에
        대한 결과를 소수점 둘째자리에서 반올림하여 실수형으로 변환하는 함수이다. 난이도:★★★★★
        여기까지 실습시간 내에 완성하시는분은 제가 소고기 사드립니다.

        ex) expCalc('1+3-5')는 -1을 반환한다.
        ex) expCalc('1+3*5')는 16을 반환한다.
        ex) expCalc('100+3+5-0')는 108을 반환한다.
        ex) expCalc('(100+3)*5+300-(200+10)/2')는 710을 반환한다.
        ex) expCalc('4+3+5/3')는 8.67을 반환한다.
        """

        numbers = []        #숫자를 저장할 리스트
        operands=[]         #연산자를 저장할 리스트
        empty_string = ""   #숫자가 2자리 이상인 경우, numbers에 저장하기 전에 전처리

        for elem in expStr:

            if elem == "(":





            #elem이 숫자인 경우, empty_string에 저장
            if elem.isdigit():
                empty_string += str(elem)
            #elem이 연산자인 경우, 그동안 받아들인 empty_string을 numbers에 저장후, elem은 operands에 저장
            #empty_string은 다시 초기화한다
            else:
                operands += str(elem)
                numbers.append(empty_string)
                empty_string = ""

        #마지막 숫자의 경우, append가 안되므로 예외처리
        numbers.append(empty_string)

        #총 연산의 횟수는 numbers에 저장된 숫자의 갯수-1이다.
        #앞에서부터 차근차근 계산을 해나간다.
        #eval()은 string을 계산처리해줌.
        for i in range(len(numbers)-1):
            result = str(numbers[i])
            temp = (eval(result + operands[i] + numbers[i+1]))
            result = temp

        print(result)

        return

calc = Calculator()
print(calc.add(1,2))
calc.subtract(3,2)

print(calc.divide(0.3,0.5))


calc.expCalc("4+3+123/2")


# ######################################################################################################################

class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

Duck1 = Duck("David")
print(Duck1.name)
Duck.name = "Kim"
print(Duck1.name)
'''
# ######################################################################################################################
import re
a = """ Rubio went after Cruz at the end of the second hour of the debate, saying that Cruz had changed his positions on immigration, trade and the military to follow shifting political winds.“I saw you on the Senate floor flip your vote on crop insurance, because they told you it would help you in Iowa,” Rubio said. “That is not consistent conservatism,” he added, using Cruz’s own slogan against him.
Cruz responded: “I appreciate you dumping your oppo [opposition] research on the debate stage,” he said, as the crowd in North Charleston, S.C., booed. “At least half the things Marco said were false.”
“You think they like each other?” Trump quipped, appearing amused as the two rivals sought to kneecap each other.”
[Still don’t think Donald Trump can win? This chart should convince you.]
The exchange came at the end of tough night for both Cruz and Rubio, first-term senators who once worked as allies but now are in each other’s way. Besides the battle between them, Cruz took criticism from Trump, and Rubio was attacked by New Jersey Gov. Chris Christie and former Florida governor Jeb Bush, his rivals in the “establishment” lane of this race.
The Fox Business GOP debate, in less than 3 minutes
Play Video2:40
Here are the key moments from the debate that brought Republican presidential candidates head-to-head in North Charleston, S.C. on Jan. 14. (Sarah Parnass/The Washington Post)
Earlier in the evening, Christie had lived up to his pugilistic reputation, threatening to kick President Obama’s “rear” at one point, and rebuking Rubio for dodging a question with a blunt “You blew it.”
“I’d like to interrupt. I’d like to interrupt. I’d like to interrupt this debate on the floor of the Senate,” Christie quipped, as Rubio and Cruz argued at length over the intricacies of their respective corporate tax proposals. He said they were trying to dodge a harder question on “entitlement” programs like Medicare and Social Security. “Do you remember that everybody? This is a question on entitlements.”
[Christie hits back: Rubio can’t ‘slime his way to the White House’]
Rubio, who had tangled with Christie earlier in the evening, tried to interrupt. Christie dismissed him: “Nah. You’ve already your chance, Marco. You blew it.”
Christie also criticized Obama for allowing states to legalize marijuana, and for undermining American’s respect for police officers – an apparent reference to Obama’s reaction to the protests over shootings by police. Obama and his allies, Christie said, “give the benefit of the doubt to the criminal. Not to the police officer.”
Click here for more information!
Earlier, Bush was strongly critical of Trump, calling his rival “unhinged” for his policies on immigration and misguided in his plans for high tariffs on Chinese imports.
“This would be devastating for our economy. We need somebody with a steady hand being president of the United States,” Bush said, after Trump said he would threaten large new tariffs on Chinese goods unless China took actions to make its trade with the U.S. more fair. Bush said it would lead to retaliatory actions by China, which would hurt U.S. exports there.
Trump responded with an attack on Bush’s personality.
“We don’t need a weak person being president of the United States,” Trump said, returning to an old insult that Bush is “low-energy.” “We don’t need that. We don’t need that.”
The crowd in North Charleston, S.C., booed at that, too – one of several times when they seemed to turn against the front-runner.
Questioning Trump’s proposal to bar Muslim foreigners from entering the United States, Bush said that it would alienate vital Muslim allies in the fight against the Islamic State.
“All Muslims? Seriously?” Bush said, in one of his strongest moments during six not-very-strong debates. “They are unhinged,” he said of Trump’s comments on the subject.
A moderator pointed out that Trump’s support had risen in South Carolina by eight points since then.
“Eleven points to be exact,” Trump interjected. He responded with a general statement of concern about Islamic terrorism: “There’s something going on, and it’s bad. We have to get to the bottom of it.”
The exchange came after Trump had rebuked Cruz for talking negatively about “New York values,” offering a tribute to the city’s response to the Sept. 11, 2001, terrorist attacks.
“When the World Trade Center came down, I saw something that no place on Earth could have handled more beautifully, more humanely than New York,” Trump said. He continued: “The people in new York fought and fought and fought, and we saw more death, and even the smell of death. Nobody understood it. And it was with us for months, the smell in the air.
That followed an attack by Cruz in which he said that “New York values” were socially liberal, and tied to money and the media. He said that Trump was representative of those values, and therefore not aligned with the values of early-voting states such as South Carolina, where the debate was held.
“I have to tell you, that was a very insulting statement that Ted made,” Trump said.
It was the second time in this debate that Cruz and Trump – who had once had an unofficial alliance, but now are rivals – had tangled, with Trump having the last word. Earlier in the debate, the two had argued about whether Cruz was even eligible to run for president, since he was born in Canada to an American mother. That led to a long exchange that allowed Trump to restate the point again and again.
[The conservative media’s civil war over Ted Cruz ‘birtherism’]
In the shadow of those two, a pair of lower-polling rivals — Christie and Rubio – each tried to cast the other as too liberal and too friendly to Obama’s priorities. Christie, in particular, responded with some unusually tough words for Obama himself.
“This guy is a petulant child,” Christie said, when asked about Obama’s efforts to circumvent Congress with executive actions to expand background checks on gun purchases. Christie then said he hoped that Obama was watching: “We are going to kick your rear end out of the White House come this fall!”
Unless Christie knows something everybody else doesn’t, Obama is not running in the election this fall. He is scheduled to leave office in January, when a new president takes office.
During the exchange about Cruz’s citizenship, Trump told Cruz that “there’s a big question mark on your head, and you can’t do that to the party.”
“Who the hell knows if you can run for office?” Trump added.
The exchange took several minutes, and also demonstrated the danger – even for a skillful debater like Cruz – of tangling with Trump, a trained master of reality TV. It began with a question for Cruz, who was born in Canada to an American mother, about whether he fit the Constitution’s definition of a “natural born” American citizen, and was eligible to run for president. He said that Trump had dismissed the idea earlier in the race but now was suddenly concerned.
“The Constitution hasn’t changed. But the poll numbers have. And I recognize that Donald is dismayed that 010.29762943@daum.net his poll numbers are falling,” Cruz said.
That set off a long exchange in which Trump admitted he had, indeed, become more concerned because of Cruz’s rise in the polls. “Because now he’s doing a little bit better. You know, I didn’t care before,” Trump said, although he also reminded Cruz that he was still ahead in the polls. “He’s got probably a 4 or 5 percent chance” of winning the race. Trump imagined a scenario in which Trump himself might choose Cruz as a running mate, “And the Democrats sue because we can’t take him along for the ride. I don’t like that.”
“I’m not going to be taking legal advice from Donald Trump,” Cruz, a Harvard Law graduate and former Supreme Court clerk, responded. Cruz said that maybe he would make Trump a vice president, which means he could benefit if Cruz was disqualified: “You can get the top job at the end of the day.”
Eventually, Rubio butted in. “I hate to interrupt this episode of Court TV.”
Earlier in the debate, Trump had called Syrian refugees a “Trojan horse” that brought terrorist sympathizers into the U.S.
“It’s reality. You just have to look today at fast_-_@ms.com Indonesia. Bombings all over. You look at California. You look, frankly, at Paris,” Trump said when asked about a refugee that President Obama had invited as his guest to the State of the Union. Trump said that refugee’s sympathetic story was not typical: “That’s not representative of what you have in that line of migration. That could be the great Trojan horse.”
Trump has said that he wants a temporary ban on all Muslim foreigners seeking to enter the U.S., and a wall to keep out undocumented immigrants along the border with Mexico. He did not appear to have changed that tactic: “We can’t let all these people come into our country and break our borders. We can’t do it.”
At one point in the debate, Cruz was asked about a New York Times report that he had failed to disclose loans made to him by Citibank and Goldman Sachs with election officials, while he ran for the Senate from Texas in 2012. Cruz later disclosed the information with Senate authorities. He rejected it as a “hit piece.”
“Yes, I made a paperwork error, disclosing it on one piece of paper instead of the other. But if that’s the best that the New York Times has got, they’d better go back to the well,” Cruz said.
Cruz began the night by criticizing Obama for failing to mention the 10 U.S. sailors who were seized – and later released – by Iranian forces in the Persian Gulf, calling it evidence of Obama’s weakness.
“We were horrified to see the sight of 10 American sailors on their knees with their hands on their head. In that state of the union, President Obama didn’t so much as mention those 10 sailors,” Cruz said, ignoring – for the moment – the fact that he had actually been asked about jobs. “It was heartbreaking. But the good news is the next commander in chief is standing on this stage.”
The sailors were later released by Iran, and the Pentagon said Thursday that they had entered Iranian territorial waters by mistake after a navigational error. But Cruz said that the sailors’ treatment – including the release of footage that showed them with hands on their heads as they were taken into custody – would have drawn a sharper response from a President Cruz.
“Any nation that captures our fighting men will feel the full force and fury of the United States of America,” Cruz said.
Later, Christie criticized Obama for underplaying the threats to the U.S.: “I watched storytime with Barack Obama.”
The main debate, which began at 9 p.m., was preceded by an “undercard” debate among former tech executive Carly Fiorina, former senator Rick Santorum (Pa.) and former Arkansas governor Mike Huckabee.
In the earlier debate, the trio of long-shot candidates offered gloomy visions of the country’s path, all hoping that they might get a ticket to the top tier of the race with just a few weeks remaining until the first votes.
Fox Business Network hosted both debates.
Cruz, in the past, had seemed reluctant to attack Trump — perhaps hoping that he would inherit Trump’s anti-establishment coalition if Trump himself faded. Now, the Texas Republican seems to have given up on that — or perhaps he is trying to hasten Trump’s fade a bit faster.
In recent days, for example, Cruz took direct aim at Trump on several fronts: tying the billionaire to Democratic presidential front-runner Hillary Clinton, questioning his ability to win a general election and casting doubt on his ability to serve as commander in chief.
Cruz also took aim at Trump’s competence. “Does a potential commander in chief know what the nuclear triad is, much less hell.xxe@gmail.com is he or she prepared and able to strengthen it and keep this country safe?” Cruz asked on “The Hugh Hewitt Show.”
In a Republican debate last month, Trump was asked about the nuclear triad — the submarines, bombers and land-based missiles that could deliver the nation’s nuclear weapons — and had trouble with the explanation.
During a campaign rally in Pensacola, Fla., on Wednesday night, Trump bragged that rivals who have dhchoi@fastcampus.co.kr attacked him in the past have seen their poll numbers tank, sometimes to the point of being pushed out of the race.
“Now, we have another debate tomorrow. They’ll all be attacking me — like, you know, they attack. Whatever. diadld2@naver.com Right? Whatever. What-ever,” Trump said, pursing his lips and shaking his head, as some in the crowd started chanting: “We want Trump! We want Trump!”
“They attack,” Trump said, “but they don’t understand that unlike this country, I attack back.”
Thursday’s main-event debate was the smallest of this crowded campaign so far: just seven candidates onstage, down from the high of 11 during a debate in September.
Sen. Rand Paul (Ky.), the libertarian-leaning candidate who battled with Rubio and Christie over their hawkish foreign policies, is sitting this one out. Paul’s polling numbers were so low he was relegated to the undercard debate. He then refused to show up at all, saying he was not running an undercard kind of campaign. He also has asked Fox to reconsider and put him on the main stage.
Although Ohio Gov. John Kasich did not figure in the more contentious exchanges, he sought to appeal directly to frustrated middle- and working-class families.
“People are upset,” he said. “You’re 50 or 51 years old and some kid walks in and tells you you’re out of work and you don’t know where to go and where to turn. Do we have an answer for that? We do.”
[Who’s got the best ground game in New yagom_123@gmail.com Hampshire? We may never know.]
Then there was Bush: once this race’s front-runner, now one of its longer shots. feedback@slack.com
Once again, he was hoping for a debate performance that will reset the race. That has not gone well in the past: In a previous debate where Bush badly wanted a breakout, he picked a fight over Rubio’s voting and attendance record in the Senate and provoked a damaging verbal takedown.
As the leading candidates feuded Thursday, Bush interjected to call for a cease-fire.
“Everybody on this stage is better than [Democratic front-runner] Hillary Clinton,” he said. “I think the focus ought to be on making sure that we leave this nomination process, as wild and woolly as it’s going to be . . . to unite behind the winner so we can defeat Hillary Clinton, because she is a disaster.”
[Bush and his super PAC are on the attack – but aiming at different targets] auction@auction.co.kr
Ben Carson, the mild-mannered neurosurgeon, seconded Bush’s call. “We have to stop this because, you know, if we manage to damage ourselves and we lose the next election and a progressive gets in there and they get two or three Supreme Court picks, this nation is over as we know it.”
Carson’s oddball campaign — which included days-long debates about whether, as a young man, he really stabbed a friend in the stomach or menaced his mother with a hammer — now seems to be fading. """

reg = "[A-Za-z0-9-_.]+@[A-Za-z0-9-._]+"
reg1 ="\S+@\S+"
print(re.findall(reg, a))
print(re.findall(reg1, a))

# ######################################################################################################################
'''
poem = "There was a young lady named Bright"
fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

fin = open('relativity', 'rb')
poem = fin.read()
fin.close()
len(poem)
print(poem)
'''

import pickle
import datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
fout = open("pickledtime", "wb")
fout.write(pickled)
fout.close()

fin=open("pickledtime", 'rb')
pickled=fin.read()
now2 = pickle.loads(pickled)
fin.close()

print(now1)
print(now2)