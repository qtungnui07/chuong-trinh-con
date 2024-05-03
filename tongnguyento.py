def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập số tự nhiên N từ người dùng
N = int(input("Nhập số tự nhiên N: "))

# Tính tổng các số nguyên tố nhỏ hơn hoặc bằng N
tong = 0
for num in range(2, N + 1):
    if la_so_nguyen_to(num):
        tong += num

# In ra tổng các số nguyên tố
print("Tổng các số nguyên tố nhỏ hơn hoặc bằng", N, "là:", tong)
