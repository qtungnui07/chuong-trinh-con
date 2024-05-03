def snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())
tong=0
for i in range(2, N + 1):
    if snt(i):
        tong+=i
if snt(tong):
    print("YES")
else:
    print("NO")