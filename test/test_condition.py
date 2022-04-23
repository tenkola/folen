def test_condition():
    flag = True
    if flag:
        print("This is true")
    else:
        print("This is False")

    assert True


def test_condition1():
    if 1 < 2:
        print("1小于2")


def test_condition_2():
    age = 30
    print("")
    if age <= 0:
        print("你是在逗我吧!")
    elif age == 1:
        print("相当于 14 岁的人。")
    elif age == 2:
        print("相当于 22 岁的人。")
    elif age > 2:
        human = 22 + (age - 2) * 5
        print("对应人类年龄: ", human)


def test_condition_3():
    """嵌套if语句"""
    num = 47
    if num % 2 == 0:
        if num % 3 == 0:
            print("你输入的数字可以整除 2 和 3")
        else:
            print("你输入的数字可以整除 2，但不能整除 3")
    else:
        if num % 3 == 0:
            print("你输入的数字可以整除 3，但不能整除 2")
        else:
            print("你输入的数字不能整除 2 和 3")
