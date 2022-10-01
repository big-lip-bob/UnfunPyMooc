count = int(input())
count = count if count >= 0 else float("inf")

sum = 0
while count > 0:
    num = input()
    if num == 'F': break
    sum += int(num)
    count -= 1

print(sum)