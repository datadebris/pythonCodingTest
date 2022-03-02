h, m, s = map(int, input().split())
rt = int(input())

rtH = int(rt / 3600)
rtM = int(rt/60) % 60
rtS = rt % 60

S2M = int((rtS + s) / 60)
M2H = int((rtM + m + S2M) / 60)

H = str(int((h + rtH + M2H) % 24))
M = str(int((rtM + m + S2M) % 60))
S = str(int((rtS + s) % 60))

print(H + " " + M + " " + S)