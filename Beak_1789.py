S = int(input())

cnt = 1

while S >= cnt:
    S -= cnt
    cnt += 1

print(cnt - 1)