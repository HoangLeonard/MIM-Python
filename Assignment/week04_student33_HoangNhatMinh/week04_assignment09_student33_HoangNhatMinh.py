
n = 1000000
count = 0
fac = 1
for i in range(1, n + 1):
    fac *= i
    while fac % 10 == 0:
        fac /= 10
        count += 1
    fac %= 10 ** (len(str(i)) + 1)



print(count)    # 249

# thuật toán đúng cho tới n = 1000

# b. chữ số tận cùng bên phải của số được tạo chính là chữ số tận cùng của biến fac mà ta đã lưu
