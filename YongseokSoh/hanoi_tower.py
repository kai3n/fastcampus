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