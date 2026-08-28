# 定义：列表是数据容器中的一类，是一次性可以存储多个数据的
# 表名称 = [元素1, 元素2, ...]
# 特点：1.可以存储多个不同类型的元素
# 2.元素有序，可以重复，元素可以修改

s = [91, 78, 27, "雷猴～", True]
print(type(s))

# 获取
print(s[0])
print(s[1])
print(s[-3])

# 修改
s[1] = 2778
s[-1] = "一键三连！！！"
print(s)

# 删除
del s[1]
print(s)

# 遍历
for item in s:
    print(item)

# 索引：前->后，从0开始；后->前，从-1开始

# 截一段出来叫 切片
# 我要把前2个拿出来，这样做
# 语句：序列数据[开始索引:结束索引:步长]
# 包小不包大

print(s[0:2:1]) # 共2+1-1个元素；+1 指索引0包进去；-1 指索引2不包进去
print(s[::-1])

# 常见方法
# 方法就是物品所具备的能力/功能

# append()：在列表的为不追加元素
# insert()：在制定索引之前，插入该元素
# remove()：移除列表中第一个匹配到的值
# pop()：删除列表中制定索引位置的元素，如未指定，默认删除最后一个
# sort()：对列表进行排序，只有数据类型一致才行
# reverse()：反转列表元素

num = [54, 78, 91, 00, 423, 27, 108, 99]
num.append(9178)
print(num)
num.insert(2, 9178)
print(num)
num.pop(3)
print(num)
num.sort()
print(num)
num.reverse()
print(num)

# 数据统计的常见语句
n = []
for i in range(11):
    n_list = int(input(f"输入10次数字：(第{i}次)"))
    n.append(n_list)
n.sort()
print("排序后的数列：", n)
print("最小值为：", n[0]) # min(n) = 本句
print("最大值为：", n[-1]) # max(n) = 本句
print("平均值为：", sum(n) / len(n))

# 解包 & 组包（不讲 ）
# 解包语句：*
n_list1 = [3425, 34, 65, 32456, 34, 5, 3456, 34]
n_list2 = [3425, 34, 65, 32456, 34, 5, 3456]
new_list = [*n_list1, *n_list2]

# 推导式
# 语句1：[要插入的值 for i in 序列/列表]
# 语句2：[要插入的值 for i in 序列/列表 if 条件]
# 找出0～100之间偶数的立方放进new列表中
new = [i ** 3 for i in range(0, 101, 2)]
print(new)