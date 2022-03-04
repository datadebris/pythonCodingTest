def printLCM(a, b):
    gcd = GCD(a, b)
    print(int(a * b / gcd))
    
def GCD(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    printLCM(a, b)