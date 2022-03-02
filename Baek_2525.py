h, m = map(int, input().split())
rt = int(input())

rtH = int(rt / 60)
rtM = rt % 60
M2H = int((rtM + m) / 60)

H = str(int((h + rtH + M2H) % 24))
M = str(int((rtM + m) % 60))

print(H + " " + M)