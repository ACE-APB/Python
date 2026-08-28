# 会有那么亿点点超纲
# 语句：if...else & if...elif...else
# 此为例子，用于理解

# 用字典存储多个账号（模拟数据库）
users = {}

print("=" * 30)
print("     欢迎来到登录系统")
print("=" * 30)

while True:
    print("\n1. 登录")
    print("2. 注册")
    print("3. 退出")
    choice = input("请选择操作（输入1/2/3）：")

    # ============ 注册 ============
    if choice == "2":
        print("\n--- 注册新账号 ---")
        account = input("请输入邮箱（如：xxx@163.com）：")

        # 检查账号是否已存在
        if account in users:
            print("该账号已注册，请直接登录！")
            continue

        pwd = input("请输入密码：")
        confirm_pwd = input("请再次确认密码：")

        if pwd == confirm_pwd:
            users[account] = pwd  # 保存到"数据库"
            print(f"注册成功！账号 {account} 已创建")
        else:
            print("两次密码不一致，注册失败！")

    # ============ 登录 ============
    elif choice == "1":
        print("\n--- 登录 ---")
        account = input("请输入邮箱：")
        pwd = input("请输入密码：")

        # 验证账号密码
        if account in users and users[account] == pwd:
            print(f"欢迎回来，{account}！")
            # 登录成功后可以在这里加后续功能
            break
        else:
            print("账号或密码错误！")

            # 找回密码
            print("\n忘记密码了？")
            find = input("输入 1 找回密码，输入 2 重新尝试：")

            if find == "1":
                if account in users:
                    new_pwd = input("请输入新密码：")
                    confirm_new = input("请再次输入新密码：")
                    if new_pwd == confirm_new:
                        users[account] = new_pwd
                        print("密码重置成功！请重新登录")
                    else:
                        print("两次输入不一致")
                else:
                    print("该账号不存在")
            # 如果选择 2，就继续循环重新登录

    # ============ 退出 ============
    elif choice == "3":
        print("再见！")
        break

    else:
        print("无效输入，请输入 1、2 或 3")