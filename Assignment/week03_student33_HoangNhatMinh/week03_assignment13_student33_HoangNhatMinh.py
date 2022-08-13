""" tìm số chữ số khi lấy 2^n ghép với 5^n
bài toán có thể giải đơn giản bằng cách chạy đoạn code:
      print(len(str(2**n) + str(5**n)))
nhưng sẽ cần tới một siêu máy tính nếu như n lớn cỡ 10000000000
"""
import itertools

"""
sau nhiều lần bằng cách thủ công, kết quả của bài toán là n + 1 đúng với n < 1000 chưa rõ với những n còn lại
"""

"""
for i in range(n)
    với cơ số 5 cứ sau iterable(2, 1, 2, 1, 2, 1, 2, 1, 1, 2).next() lần tăng của n thì số chữ số tăng lên 1 (i != 0)
    với cơ số 2 cứ sau iterable(4, 3, 3).next() lần tăng của n thì số chữ số tăng lên 1 vói mọi i
    # chưa chứng minh được.

ta biểu diễn 2 iterable đó như sau:
"""
# cách 1
base5 = itertools.cycle([1,0, 1, 1,0, 1, 1,0, 1, 1,0, 1, 1, 1,0, 1])
base2 = itertools.cycle([1,0,0,0, 1,0,0, 1,0,0])
n = 100
total = 0
exp5 = 0
exp2 = 0
for i in range(0, n+1):
    exp2 = exp2 + base2.__next__()
    if i == 0:
        exp5 = exp5 + 1
    else:
        exp5 = exp5 + base5.__next__()
    total = exp5 + exp2

print(total)
# cách 2
print(n+1)
