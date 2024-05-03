def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập số nguyên dương từ người dùng
N = int(input("Nhập một số nguyên dương N: "))

# Tính tổng các chữ số của N
tong = sum(int(digit) for digit in str(N))

# Kiểm tra xem tổng của các chữ số có phải là số nguyên tố hay không và in ra kết quả
if la_so_nguyen_to(tong):
    print("Tổng các chữ số của", N, "là", tong, "và là số nguyên tố.")
else:
    print("Tổng các chữ số của", N, "là", tong, "và không phải là số nguyên tố.")
