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


import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b ** 2) - (4 * a * c)

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)      # 二次方程式 ax**2 + bx + c = 0
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为 {0} 和 {1}'.format(sol1, sol2))
