from operator import index

# for i in range(0,2):
#     for j in range(3,5):
#         print(j)
#     print(i)


# print("/n Loop in loop 1:")
# for i in range(0,2):
#     print(i)
#     for j in range(3,5):
#         print(j)
#
# print("/n Loop in loop 2:")
# for i in range(0,2):
#     for j in range(3,5):
#         print(j)
#     print(i)
#
# print("/n Loop in loop 3:")
# for i in range(0,2):
#     for j in range(3,5):
#         print(j)
#         print(i)
s_denominator = 0
for i in range(100):
    if i==1:
        continue
    #  có thể sài cách khác for i in range(1,100,2): cách lấy số cách nhau mà kh cần dùng continue và module
    if i % 2 == 0:
        continue
    s_denominator += 1/i
#     viết tắt của (s_denominator= s_denominator + 1/i)

s = 1/s_denominator
s = round(s,2)
# cách lấy 2 số thập phân
print(s)
