count = int(input())
sum = 0

for _ in range(0, count if count >= 0 else 1 << 40) and (num := input()) != 'F': sum += int(num)

print(sum)