n = int(input())

for y in range(0, n):
    print(' ' * (n - y - 1), end = '')
    for x in range(y):
        print((x + y + 1) % 10, end = '')
    for x in range(y, -1, -1):
        print((x + y + 1) % 10, end = '')
    print()