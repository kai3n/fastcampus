def _printstar(n):

    for i in range((n-1), -1, -1):

        for j in range(0, i):
            print(" ", end = "")

        for j in range(i, n):
            print("*", end = "")
        print()

_printstar(10)

def _printTree(n):

    for i in range(1, n+1):

        for j in range(0, n-i+1):
            print(" ", end = "")
        for j in range(n-i+1, n+i):
            print ("*", end = "")
        for j in range(n+i,2*n+1):
            print (" ", end = "")
        print()

_printTree(10)

def _numTree(n):

    number = n*n

    for i in range(1, n+1):

        for j in range(0, n-i+1):
            print(" ", end = "")
        for j in range(n-i+1, n+i):
            print (number, end = "")
            number = number-1
        for j in range(n+i,2*n+1):
            print (" ", end = "")
        print()

_numTree(3)


def _spiralMatrix(n):
    a = [[0 for i in range(n)] for i in range(n)]

    degree = (n+1)/2
    total = n*n

    for i in range(1, n*n):

        for j in range(n, 1, -2):







