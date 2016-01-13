#글자 수 세기
#특정 문자열을 매개변수로 넣기 매개변수로 넣으면 길이를 반환

#a = 'python is too hard'
#print(a.count(''))

def word_count(word):
 word_cnt=word.split(" ")

 return len(word_cnt)

print(word_count('python is too hard'))



