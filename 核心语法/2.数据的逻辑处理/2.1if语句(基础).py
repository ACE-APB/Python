# 顾名思义，if译为“如果”
# 只有满足指定条件，才会执行对应代码逻辑

# 格式：
# if 条件:
#     执行的代码...

pwd = input("欢迎注册！请输入密码：")
pwd = int(pwd)
pwd_1 = input("欢迎登陆！请输入密码：")
pwd_1 = int(pwd_1)
if pwd == pwd_1:
    print("欢迎！！！")
if pwd != pwd_1:
    print("Error！")