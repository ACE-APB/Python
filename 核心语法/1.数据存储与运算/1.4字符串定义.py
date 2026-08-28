# 字符串有三种定义

# 1.双引号
s1 = "hello"

# 2.单引号
s2 = 'hello'

# 3.三引号
s3 = """
hello
一键三连！！！
"""

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

# 进阶版

  # 转义符
# \' 表示单引号
# \" 表示双引号
# \n 换行符
# \t 制表符 缩进一个tab的大小

print('It\'s very easy!')
print('It\'s very \neasy!')
print('It\'s very\teasy!')

  # 混合使用
print("It's very easy!")