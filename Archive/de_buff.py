z = 1


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
    global z, n
    max_num = 1
    min_num = 0
    flag = True
    num = 1
    # 使用二分查找
    while flag:
        z = (max_num + min_num) / 2

        num += 1
        for ls in sg:
            c = count_buff(*ls[:-1]) - ls[-1]
            print(f'{z:.35f}', '误差:', c)
            if c < -n:
                min_num = z
                flag = True
            elif c > n:
                max_num = z
                flag = True

            else:
                flag = False
        if num > 100:
            n += 1
            num = 1


BASIC_DATA = [154, 164, 176, 186, 197, 206, 216, 227, 237, 249, 259, 269, 280, 290,
              302, 311, 321, 332, 342, 353, 363, 374, 385, 395, 406, 415, 425, 437,
              447, 458, 468, 478, 489, 500, 511, 520, 530, 541, 551, 563]



sg = [
    # [等级, 增益量, 适用智力, 实际理智]
    [31, 177064, 8392, 77755],
    [32, 177064, 8392, 79416],
    [21, 177064.8, 8712, 61821],
    [33, 177064.8, 8392, 81244],
    [20, 160968, 8606, 54869],
    [32, 160968, 8267, 72351],
    [23, 160968, 8267, 58274],
]

# sg_ = [
#     # [等级, 增益量, 适用智力, 实际三攻]
#     [36, 125622, 9373, 12278],
#     [20, 125622, 8343, 8333],
#     [32, 125622, 8110, 10431],
#     [23, 125622, 8110, 8653],
#     [33, 125622, 8195, 10622],
#     [1, 25434, 3232, 819],
#
# ]

# 不要穿戴任何百分比加成的装备(光环,宠物,辟邪玉)来填写数值
n = 0  # 误差
binary_de()
print('----------------------------------------------------')
print(f'Z={z:.35f}', '科学计数', z, '误差', n)
