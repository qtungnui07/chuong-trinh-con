def snt(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input("Nhập số tự nhiên N: "))
k = 0

for num in range(1, N + 1):
    if N%num==0:
        k += 1

if snt(k):
    print("YES")
else:
    print("NO")
