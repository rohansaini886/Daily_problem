for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(' ')))
    a, b = 0, 0
    for i in  l:
        if i > a:
            a, b = i, a
        elif i > b:
            b = i
    # print(a, b)
    for i in l:
        if i == a:
            print(a - b, end = ' ')
        else:
            print(i - a, end = ' ')
    print()
