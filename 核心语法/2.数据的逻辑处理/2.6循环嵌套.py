# for语句：
# for 元素 in 待处理数据集1:
#     循环体
#     ...
#     for 元素 in 待处理数据集2:
#         循环体
#         ...

# 做一个n*n三角形
n = int(input())
for j in range(n + 1):
    for i in range(j):
        print("*", end=" ")
    print()