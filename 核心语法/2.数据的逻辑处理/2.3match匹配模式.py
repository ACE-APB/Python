# 之前学了if，可是有时候很麻烦，我的例子就是(不是下面的例子)
# 例子文件：2.3.1match匹配例子.py

# 语句：match...case
# C++：switch...case
# 结构模式匹配就是用一个清晰的 模板 去精准的匹配数据的结构和内容，匹配成功则执行相应的操作

# 如果前面的情况都没有匹配到，默认执行case _，等同于else

day = "周六"
weather = "晴天"

match (day, weather):
    case ("周六", "晴天"):
        print("去爬山")
    case ("周日", "晴天"):
        print("去爬山")
    case ("周六", "雨天"):
        print("在家看电影")
    case ("周日", "雨天"):
        print("在家看电影")
    case (_, "晴天"):
        print("去上班/上学")
    case (_, "雨天"):
        print("带伞出门")