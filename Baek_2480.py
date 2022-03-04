# 주사위 세개 입력 받기
from tkinter.tix import MAX


a, b, c = map(int, input().split())

# 상금 저장용 변수
sum = 0

# 1. 세개의 눈이 같을 때 상금
# 10,000원 + (같은 눈) * 1,000원
if a == b & b == c:
    sum = 10000 + a * 1000

# 2. 같은 눈이 두개만 나올 때
elif a == b & a != c:
    sum = 1000 + a * 100

elif a == c & b != c:
    sum = 1000 + a * 100

elif a != b & b == c:
    sum = 1000 + b * 100

# 3. 같은 눈이 하나도 없을때
else:
    sum = max(a, b, c)  * 100


print(sum)