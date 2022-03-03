sum = 0

for _ in range(5):
    x = int(input())
    if x > 40:
        sum += x
    else:
        sum += 40

print(int(sum / 5))