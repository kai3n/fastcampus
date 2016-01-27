def hanoi(n, start=1, end=3):
    if n:
        hanoi(n-1, start, 6-end-start)
        print("{}번 디스크를 {}번 폴대에서 {}번 폴대로 옮기시오".format(n, start, end))
        hanoi(n-1, 6-end-start, end)

hanoi(3)