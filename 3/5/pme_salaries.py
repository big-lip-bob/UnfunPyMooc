sum = 0
count = 0

while (num := int(input())) >= 0:
    sum += num
    count += 1

print(sum / count)