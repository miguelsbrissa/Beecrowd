x1, y1, x2, y2 = map(int, input().split())

def testaDiagonal(x1, y1, x2, y2):
    flag = False
    tempx1 = x1
    tempy1 = y1

    while tempx1 != 1 and tempy1 != 1:
        tempx1 -= 1
        tempy1 -= 1
        if tempx1 == x2 and tempy1 == y2:
            flag = True
            

    while tempx1 != 8 and tempy1 != 8:
        tempx1 += 1
        tempy1 += 1
        if tempx1 == x2 and tempy1 == y2:
            flag = True

    tempx1 = x1
    tempy1 = y1

    while tempx1 != 1 and tempy1 != 8:
        tempx1 -= 1
        tempy1 += 1
        if tempx1 == x2 and tempy1 == y2:
            flag = True
            

    while tempx1 != 8 and tempy1 != 1:
        tempx1 += 1
        tempy1 -= 1
        if tempx1 == x2 and tempy1 == y2:
            flag = True
            

    return flag

while x1 != 0 or y1 != 0 or x2 != 0 or y2 != 0:
    if x1 == x2 and y1 == y2:#mesma posicao
        print(0)
    elif x1 == x2 or y1 == y2:#mesma linha ou coluna
        print(1)
    elif testaDiagonal(x1, y1, x2, y2):
        print(1)
    else:
        print(2)

    x1, y1, x2, y2 = map(int, input().split())