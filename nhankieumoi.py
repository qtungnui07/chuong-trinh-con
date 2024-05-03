a=int(input())
b=int(input())
tong=0
for digit_a in str(a):
    for digit_b in str(b):
        tong+=int(digit_a)*int(digit_b)
        
print(tong)