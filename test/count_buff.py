import decimal

import sys  # 导入sys模块

import sympy as sympy

z = 1
BASIC_DATA = {
    'nai_ma': {
        'san_gong': [39, 41, 43, 44, 45, 47, 49, 50, 52, 53, 54, 56, 58, 59, 61, 62,
                     63, 65, 67, 69, 70, 71, 73, 75, 77, 79, 80, 81, 83, 85, 86, 88,
                     89, 90, 92, 94, 95, 97, 98, 100]
        ,
        'li_zhi': [154, 164, 176, 186, 197, 206, 216, 227, 237, 249, 259, 269, 280, 290,
                   302, 311, 321, 332, 342, 353, 363, 374, 385, 395, 406, 415, 425, 437,
                   447, 458, 468, 478, 489, 500, 511, 520, 530, 541, 551, 563]

    },
    'nai_ba': {
        'san_gong': [44, 45, 47, 49, 50, 52, 54, 55, 57, 59, 60, 62, 64, 65, 67, 69,
                     70, 72, 74, 77, 78, 80, 82, 83, 85, 87, 88, 90, 92, 93, 95, 97,
                     98, 100, 102, 103, 105, 107, 108, 111]
        ,
        'li_zhi': [171, 182, 193, 206, 217, 228, 239, 251, 263, 275, 286, 297, 310, 321,
                   333, 343, 355, 367, 379, 390, 401, 414, 425, 437, 448, 459, 471, 483,
                   494, 505, 518, 529, 541, 552, 565, 575, 587, 598, 609, 622]

    },
    'nai_luo': {
        'san_gong': [34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54,
                     55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76,
                     77, 78, 80, 81, 82, 84, 85, 87],
        'li_zhi': [131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247,
                   256, 264, 273, 282, 291, 300, 309, 318, 327, 336, 345, 353, 362, 371,
                   380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478],
    },
    "tai_yang": [43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379,
                 414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939, 993,
                 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668]
}


def count_buff(lv, buff_amount, intellect, attack_fixed):
    basic_attack = BASIC_DATA['nai_ma']['san_gong'][lv - 1]

    xs = 665
    x, y = (4350, 3500)
    old_buff = (basic_attack + attack_fixed) * ((intellect / xs) + 1)

    new_buff = basic_attack * ((intellect + x) / xs + 1) * (
            buff_amount + y) * z if buff_amount != 0 else 0

    buff = (old_buff + new_buff) * (1.08 if buff_amount != 0 else 1)
    return round(buff)


def binary_de():
    global z
    max_num = 1
    min_num = 0
    flag = True
    while flag:
        z = (max_num + min_num) / 2

        for ls in sg:
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
    print(z)


sg = [
    [35, 111806, 8845, 8, 10591],
    [35, 111806, 8840, 8, 10587],
    [33, 111806, 7935, 8, 9532],
    [21, 107883, 8061, 8, 7378],
    [18, 99319, 7624, 8, 6180],
    [35, 106741, 8729, 8, 10102],
    [35, 111683, 8840, 8, 10577],
    [10, 89060, 7209, 8, 4470],
    [10, 16960, 3272, 8, 943],
    [21, 91322, 7265, 0, 5917],
    [23, 107883, 8061, 8, 7690],
    [33, 80486, 7178, 8, 6843],
    [37, 111806, 8885, 8, 10966],
    [21, 102824, 8053, 8, 7089],
    [15, 107764, 8061, 0, 6325],
    [33, 106741, 7897, 8, 9144],
    [6, 17808, 3654, 8, 920],
    [33, 111683, 7935, 8, 9523],
    [33, 111806, 7935, 8, 9532],
    [33, 111683, 7935, 8, 9523],

]
#  [等级, 增益量, 力智, 固定玉, 实际三攻]
# 添加任何错误的值都会导致死循环
# 不建议穿戴任何百分之加成的装备(光环,宠物,辟邪玉)填写数值

binary_de()
