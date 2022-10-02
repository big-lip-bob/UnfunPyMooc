num = int(input())
sum = 0
if num < 0:
    while (num := input()) != "F": sum += int(num)
else:
    for i in range(0, num): sum += int(input())
print(sum)