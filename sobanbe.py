m,n=map(int,input().split())
tong1=0
tong2=0
for i in range(1,m):
    if m%i==0:
        tong1+=i
for j in range(1,n):
    if n%j==0:
        tong2+=j

if tong1==n and tong2==m:
    print("YES")
else:
    print("NO")
    
    
    
    
m, n = map(int, input().split())

# Tính tổng các ước của m và n
tong_1 = sum([i for i in range(1, m) if m % i == 0])
tong_2 = sum([j for j in range(1, n) if n % j == 0])

# Kiểm tra xem tổng các ước của m có bằng n và tổng các ước của n có bằng m không
if tong_1 == n and tong_2 == m:
    print("YES")
else:
    print("NO")
