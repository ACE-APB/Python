# We know，有many符号，大致分为（部分）
# 算术运算符：+ - * /
# 赋值运算符：=
# 比较运算符：< > >= <= !=
# 逻辑运算符：or and

# 1.算术运算符
# 有：+(加) -(减) *(乘) /(除) //(整除) %(取余/求mod) **(幂指数)
# 优先级：() > ** > * / // % > + -

print("91 + 78 = {}".format(91 + 78))
print("91 - 78 = {}".format(91 - 78))
print("91 * 78 = {}".format(91 * 78))
print("91 / 78 = {}".format(91 / 78))
print("91 // 78 = {}".format(91 // 78))
print("91 % 78 = {}".format(91 % 78))
print("91 ** 78 = {}".format(91 ** 78))

x, y = input("请输入").split()
x = float(x)
y = float(y)
print(x + y)
print(x - y)

# 2.赋值运算符
# 有：= += -= *= /= %= //= **=

num = 10.0

num += 5
print(num)
num -= 5
print(num)
num *= 5
print(num)
num /= 5
print(num)
num **= 5
print(num)
num //= 5
print(num)
num %= 5
print(num)

# 3.比较运算符
# 有：== !=(不等于) > >= < <=
# 返回bool值

a = 9178
b = 2778
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 4.逻辑运算符
# 有：and or not
# C++：&& || ~

num = float(input("输入："))
print(f"{num}在10-20之间？：", num >= 10.0 and num <= 20.0)
print(f"{num}不在10-20之间？：", num < 10.0 or num > 20.0)