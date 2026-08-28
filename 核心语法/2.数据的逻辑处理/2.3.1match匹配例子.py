# 题目参考：务业.png

# match写法 44行 优雅～
def calc_shipping_match(member, amount, method, is_remote, is_hmt):
    match (member, amount, method, is_remote, is_hmt):
        # 特殊地区优先
        case (_, _, _, _, True):
            return 60

        # 金牌会员
        case ("gold", amount, _, _, False) if amount >= 200:
            return 0
        case ("gold", _, "normal", False, False):
            return 5
        case ("gold", _, "normal", True, False):
            return 15
        case ("gold", _, "express", False, False):
            return 20
        case ("gold", _, "express", True, False):
            return "不可配送"

        # 银牌会员
        case ("silver", amount, "normal", False, False) if amount >= 150:
            return 8
        case ("silver", amount, "normal", True, False) if amount >= 150:
            return 18
        case ("silver", amount, "express", False, False) if amount >= 150:
            return 25
        case ("silver", amount, "express", True, False) if amount >= 150:
            return "不可配送"
        case ("silver", _, _, _, False):
            return 30  # 金额<150，任何方式

        # 铜牌会员
        case ("bronze", amount, "normal", False, False) if amount >= 100:
            return 10
        case ("bronze", amount, "normal", True, False) if amount >= 100:
            return 25
        case ("bronze", amount, "express", False, False) if amount >= 100:
            return 35
        case ("bronze", amount, "express", True, False) if amount >= 100:
            return "不可配送"
        case ("bronze", _, _, _, False):
            return 40

        case _:
            return "无效会员"

# if写法 50行 丑陋～
def calc_shipping_if(member, amount, method, is_remote, is_hmt):
    # 特殊地区优先
    if is_hmt:
        return 60
    else:
        # 会员等级分支
        if member == "gold":
            if amount >= 200:
                return 0
            else:
                if method == "normal":
                    if is_remote:
                        return 15
                    else:
                        return 5
                else:  # 加急
                    if is_remote:
                        return "不可配送"
                    else:
                        return 20
        elif member == "silver":
            if amount >= 150:
                if method == "normal":
                    if is_remote:
                        return 18
                    else:
                        return 8
                else:
                    if is_remote:
                        return "不可配送"
                    else:
                        return 25
            else:
                return 30
        elif member == "bronze":
            if amount >= 100:
                if method == "normal":
                    if is_remote:
                        return 25
                    else:
                        return 10
                else:
                    if is_remote:
                        return "不可配送"
                    else:
                        return 35
            else:
                return 40
        else:
            return "无效会员"