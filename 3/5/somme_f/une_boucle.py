count = int(input())
count = count if count >= 0 else 1 << 40

sum = 0
for _ in range(0, count):
    num = input()
    if num == 'F': break
    sum += int(num)
    count -= 1

print(sum)