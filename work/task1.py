"""
python基础
"""


# 1. 搭建个人博客 参考: https://onefeng.xyz/2021/07/10/jekyll/

# 2. 定义一个函数判断一个数是否为素数。提示：需要用到for循环,if语句
def is_number(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True
