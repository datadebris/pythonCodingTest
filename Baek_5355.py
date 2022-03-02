n = int(input())

for _ in range(n):
    x = input().split()
    ans = float(x[0])
    for j in range(len(x) - 1):
        if x[j + 1] == "@":
            ans *= 3
        elif x[j + 1] == "%":
            ans += 5
        elif x[j + 1] == "#":
            ans -= 7
    print("{:.2f}".format(ans))

    # 소수점 관리하는 방법

    # round(num, 위치)
    # {:.위치f}.format(num)
    # {num:.위치f}