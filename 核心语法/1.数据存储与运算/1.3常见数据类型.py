# 可以通过 type() 语句来得到数据的类型
print(type("hello"))
print(type(10))
print(type(3.14))
print(type(True))
print(type(None))

# 可以通过 isinstance() 检查数据是否属于指定类型，返回的是bool值
# 语法：isinstance(数据, 类型)
num = 5.0
print(isinstance(num, float))
print(isinstance(num, int))