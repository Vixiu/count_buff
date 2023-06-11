import sympy

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
    'nai_gong':
        {
            'san_gong': [34, 35, 37, 38, 39, 41, 42, 43, 45, 56, 47, 49, 50, 51, 53, 54,
                         55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76,
                         77, 78, 80, 81, 82, 84, 85, 87],
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


def de_buff(lv, buff_amount, intellect, attack_fixed, buff):
    x = sympy.Symbol('x')
    #  basic_attack = round((1.34631476716774 * lv + 32.600) * 1.131 * 1.02)
    basic_attack = BASIC_DATA['nai_ma']['san_gong'][lv - 1]
    print(sympy.solve(
        (((basic_attack + attack_fixed) * ((x / 665) + 1)) +
         (basic_attack * ((x + 4345) / 665 + 1) * (
                 buff_amount + 3500) * 0.0000379)) * 1.08 -
        buff,
        x))


def count_buff(lv, buff_amount, intellect, attack_fixed):
    print(buff_amount)
    cr = 'nai_gong'
    xs = 665
    x, y = (4350, 3500)
    # basic_attack = (1.34 * lv + 32.600) * 1.131 * 1.02
    basic_attack = BASIC_DATA[cr]['san_gong'][lv - 1]
    basic_attack = 56
    print(basic_attack)
    old_buff = ((basic_attack + attack_fixed) * ((intellect / xs) + 1))
    new_buff = basic_attack * ((intellect + x) / xs + 1) * (
            buff_amount + y) * z if buff_amount != 0 else 0
    buff = (old_buff + new_buff) * (1.08 if buff_amount != 0 else 1)

    return round(buff)


def count_lz(lv, buff_amount, intellect, attack_fixed):
    basic_attack = BASIC_DATA['nai_ma']['li_zhi'][lv - 1]
    old_buff = ((basic_attack + attack_fixed) * ((intellect / 665) + 1))
    new_buff = basic_attack * ((intellect + 4350) / 665 + 1) * (
            buff_amount + 3500) * z if buff_amount != 0 else 0
    buff = (old_buff + new_buff) * (1.08 if buff_amount != 0 else 1)
    return round(buff)


def count(a, b):
    if a != b:
        print(f'应为:{b},实际:{a}，相差:{b - a}')


z = 0.00003788627

count(count_buff(11, 15527, 2526, 0), 785)

'''
count(count_buff(35, 111806, 8845, 8, 1, 1, 1, 1, 1), 10591)

count(count_buff(35, 111806, 8840, 8, 1, 1, 1, 1, 1), 10587)


count(count_lz(21, 111806, 8066, 0), 58141)
count(count_lz(35, 111806, 8845, 0), 58141)
count(count_lz(33, 111806, 7935, 0), 51758)
count(count_lz(21, 107883, 8061, 0), 37675)
count(count_lz(19, 107883, 8061, 0), 35495)
count(count_lz(12, 107883, 8061, 0), 27919)

count(count_buff(33, 111806, 7935, 8, 1, 1, 1, 1, 1), 9532)
count(count_buff(21, 107883, 8061, 8, 1, 1, 1, 1, 1), 7378)
count(count_buff(18, 99319, 7624, 8, 1, 1, 1, 1, 1), 6180)
count(count_buff(18, 107883, 8061, 8, 1, 1, 1, 1, 1), 6860)
count(count_buff(35, 106741, 8729, 8, 1, 1, 1, 1, 1), 10102)
count(count_buff(35, 111683, 8840, 8, 1, 1, 1, 1, 1), 10577)
count(count_buff(10, 89060, 7209, 8, 1, 1, 1, 1, 1), 4470)
count(count_buff(10, 16960, 3272, 8, 1, 1, 1, 1, 1), 943)
count(count_buff(21, 91322, 7265, 0, 1, 1, 1, 1, 1), 5917)
count(count_buff(23, 107883, 8061, 8, 1, 1, 1, 1, 1), 7690)
count(count_buff(33, 80486, 7178, 8, 1, 1, 1, 1, 1), 6843)
count(count_buff(37, 111806, 8885, 8, 1, 1, 1, 1, 1), 10966)
count(count_buff(21, 102824, 8053, 8, 1, 1, 1, 1, 1), 7089)
count(count_buff(15, 107764, 8061, 0, 1, 1, 1, 1, 1), 6325)
count(count_buff(33, 106741, 7897, 8, 1, 1, 1, 1, 1), 9144)
count(count_buff(6, 17808, 3654, 8, 1, 1, 1, 1, 1), 920)

count(count_buff(1, 0, 2324, 0, 1, 1, 1, 1, 1), 175)
count(count_buff(14, 0, 3905, 8, 1, 1, 1, 1, 1), 460)
count(count_buff(12, 0, 3905, 8, 1, 1, 1, 1, 1), 440)
count(count_buff(10, 0, 3905, 8, 1, 1, 1, 1, 1), 419)
count(count_buff(5, 0, 3905, 8, 1, 1, 1, 1, 1), 364)

count(count_buff(33, 111683, 7935, 8, 1, 1, 1, 1, 1), 9523)
count(count_buff(33, 111806, 7935, 8, 1, 1, 1, 1, 1), 9532)
'''