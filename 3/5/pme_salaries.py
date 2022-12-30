sum, count = 0, 0

while (num := int(input())) >= 0:
    sum += num
    count += 1

print(count and sum / count)