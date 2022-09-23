num = int(input())
sum = 0
if num < 0:
    while True:
        num = input()
        if num == "F": break
        sum += int(num)
else:
    for i in range(0, num): sum += int(input())
print(sum)