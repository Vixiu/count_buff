BASIC_DATA = {
    'nai_ma': {
        'san_gong': [39, 41, 43, 44, 45, 47, 49, 50, 52, 53, 54, 56, 58, 59, 61, 62,
                     63, 65, 67, 69, 70, 71, 73, 75, 77, 79, 80, 81, 83, 85, 86, 88,
                     89, 90, 92, 94, 95, 97, 98, 100],
        'li_zhi': [154, 164, 176, 186, 197, 206, 216, 227, 237, 249, 259, 269, 280, 290,
                   302, 311, 321, 332, 342, 353, 363, 374, 385, 395, 406, 415, 425, 437,
                   447, 458, 468, 478, 489, 500, 511, 520, 530, 541, 551, 563],
        'xs': 665,
        'attack_xyz': (4345, 3500, 0.0000379),
        'intellect_xyz': (4345.545, 3500, 0.0000379)
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
data = {
    'buff_amount': 111806,
    'out_intellect': 7935,
    'out_lv': 33,
    'in_intellect': 0,
    'in_lv': 1,
    #   'in_ty_lv': 1,
    'halo_amount': 0,
    'pet_amount': 0,
    'jade_amount': 0,
    'fixed_attack': 8,
    'fixed_intellect': 0,
    'percentage_attack': [],
    'percentage_intellect': [],
    # 'cp_arms': True
}


def count_buff(lv, buff_amount, intellect, cp_arms=True):
    def count(fixed, bfb, xs, xyz):
        x, y, z = xyz
        basic_attack = BASIC_DATA['nai_ma']['san_gong'][int(lv - 1)]
        old_buff = ((basic_attack + fixed) * ((intellect / xs) + 1))
        for n in bfb:
            old_buff *= (1 + n / 100)
        new_buff = basic_attack * ((intellect + x) / xs + 1) * (buff_amount + y) * z if buff_amount != 0 else 0
        buff = (old_buff + new_buff) * (1.08 if cp_arms else 1)
        return round(buff)

    return count


def count_zj_buff(cr):
    count = count_buff(
        data['out_lv'],
        data['buff_amount'] * (1 + data['halo_amount'] / 100 + data['pet_amount'] / 100),
        data['out_intellect'],
    )

    return count(
        data['fixed_attack'],
        data['percentage_attack'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['attack_xyz'],
    ), count(
        data['fixed_intellect'],
        data['percentage_intellect'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['intellect_xyz'],
    )


def count_jt_buff(cr):
    count = count_buff(
        data['in_lv'],
        data['buff_amount'] * (1 + data['halo_amount'] / 100 + data['pet_amount'] / 100+data['jade_amount'] / 100),
        data['in_intellect'],
    )

    return count(
        data['fixed_attack'],
        data['percentage_attack'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['attack_xyz'],
    ), count(
        data['fixed_intellect'],
        data['percentage_intellect'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['intellect_xyz'],
    )


print(count_zj_buff('nai_ma'))
