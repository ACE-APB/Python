# while循环是通过条件表达式来控制是否要进行下一次循环的。而for循环，本质就是一种轮询遍历机制，对一批内容进行逐个处理

# 语句：
# for 元素 in 待处理数据集:
#     循环体
# else:
#     代码

meg = "Hello ACE-APB"
for i in meg:
    print(i)
else:
    print("一键三连！！！")

# range语句
# 作用：生成指定规则的数字序列
# 用法：
# 1.range(end) -> 0~end-1
# 2.range(start, end) -> start~end-1
# 3.range(start, end, step) -> start~end-1 & n = start + step
# C++: for(int i = 1; i <= n; i++){} （不是唯一，学过的都知道～）

total = 0
for i in range(1, 101, 2):
    total = total + i
print(total)