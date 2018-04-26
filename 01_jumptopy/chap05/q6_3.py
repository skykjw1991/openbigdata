def getTotalPage(m,n):
    if m > n:
        if m % n == 0:
            return int(m / n)
        else:
            return int(m / n) + 1
    elif m == 0:
        return m
    else:
        return int(1)

f = open('D:\\bigdata\\python_workspace\\openbigdata\\01_jumptopy\\chap05\\condition.txt', 'r')
while True:
    try:
        line = f.readline().split()
        if len(line) == 0:
            break
        a = line[0]
        b = line[1]
        print("게시물 총 건수: %d, 한 페이지에 보여줄 게시물 수: %d, 총 페이지수: %s" % (int(a), int(b), getTotalPage(int(a),int(b))))
    except ValueError or IndexError:
        pass
f.close()
