z = 1
BASIC_DATA = [39, 41, 43, 44, 45, 47, 49, 50, 52, 53, 54, 56, 58, 59, 61, 62,
              63, 65, 67, 69, 70, 71, 73, 75, 77, 79, 80, 81, 83, 85, 86, 88,
              89, 90, 92, 94, 95, 97, 98, 100]


def count_buff(lv, buff_amount, intellect):
    basic_attack = BASIC_DATA[lv - 1]

    xs = 665
    x, y = (4350, 3500)
    old_buff = basic_attack * ((intellect / xs) + 1)

    new_buff = basic_attack * ((intellect + x) / xs + 1) * (
            buff_amount + y) * z if buff_amount != 0 else 0

    buff = (old_buff + new_buff) * (1.08 if buff_amount != 0 else 1)
    return round(buff)


def binary_de():
    global z
    max_num = 1
    min_num = 0
    flag = True
    num = 1
    # 使用二分查找
    while flag:
        z = (max_num + min_num) / 2
        for ls in sg:
            num += 1
            c = count_buff(*ls[:-1]) - ls[-1]
            if c < 0:
                min_num = z
                flag = True
                break
            elif c > 0:
                max_num = z
                flag = True
                break
            elif c == 0:
                flag = False
    print(z, f'运算{num}次')


sg = [
    [36, 125622, 9373, 12278],
    [20, 125622, 8343, 8333],
    [32, 125622, 8110, 10431],
    [23, 125622, 8110, 8653],
    [33, 125622, 8195, 10622],
    [1, 25434, 3232, 819],
    # [等级, 增益量, 适用智力, 实际三攻]
]
# [等级, 增益量, 适用智力, 实际三攻]
# 添加任何错误的值都会导致死循环
# 不要穿戴任何百分比加成的装备(光环,宠物,辟邪玉)来填写数值

binary_de()
