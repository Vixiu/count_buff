import json
from os import getenv, path, makedirs
from sys import argv
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog, QLineEdit, QGraphicsDropShadowEffect
from BuffUI import BuffUI, RoundedWindow
from PyQt5.QtCore import Qt

BUFF_BASE = {
    'nai_ma': {
        'san_gong': [39, 41, 43, 44, 45, 47, 49, 50, 52, 53, 54, 56, 58, 59, 61, 62,
                     63, 65, 67, 69, 70, 71, 73, 75, 77, 79, 80, 81, 83, 85, 86, 88,
                     89, 90, 92, 94, 95, 97, 98, 100],
        'li_zhi': [154, 164, 176, 186, 197, 206, 216, 227, 237, 249, 259, 269, 280, 290,
                   302, 311, 321, 332, 342, 353, 363, 374, 385, 395, 406, 415, 425, 437,
                   447, 458, 468, 478, 489, 500, 511, 520, 530, 541, 551, 563],
        'xs': 665,
        'xyz': (4350, 3500, 3.78880649805069e-05),
    },
    'nai_ba': {
        'san_gong': [44, 45, 47, 49, 50, 52, 54, 55, 57, 59, 60, 62, 64, 65, 67, 69,
                     70, 72, 74, 77, 78, 80, 82, 83, 85, 87, 88, 90, 92, 93, 95, 97,
                     98, 100, 102, 103, 105, 107, 108, 111],
        'li_zhi': [171, 182, 193, 206, 217, 228, 239, 251, 263, 275, 286, 297, 310, 321,
                   333, 343, 355, 367, 379, 390, 401, 414, 425, 437, 448, 459, 471, 483,
                   494, 505, 518, 529, 541, 552, 565, 575, 587, 598, 609, 622],
        'xs': 620,
        'xyz': (4345, 3498, 0.000035699),

    },
    'nai_gong': {
        'san_gong': [40, 42, 44, 46, 47, 49, 51, 52, 54, 55, 56, 58, 60, 61, 63,
                     64, 65, 67, 70, 72, 73, 74, 76, 78, 80, 82, 83, 84, 86, 88,
                     89, 92, 93, 94, 96, 98, 99, 101, 102, 104],
        'li_zhi': [162, 173, 186, 196, 207, 217, 227, 239, 249, 262, 272, 283,
                   295, 306, 318, 328, 338, 350, 360, 372, 382, 394, 406, 416,
                   428, 437, 448, 460, 471, 482, 493, 503, 516, 527, 539, 548,
                   559, 570, 581, 593]
        ,
        'xs': 665,
        'xyz': (4350, 3500, 3.78880649805069e-05),

    },
    'nai_luo': {
        'san_gong': [34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54,
                     55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76,
                     77, 78, 80, 81, 82, 84, 85, 87],
        'li_zhi': [131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247,
                   256, 264, 273, 282, 291, 300, 309, 318, 327, 336, 345, 353, 362, 371,
                   380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478],
        'xs': 665,
        'xyz': (4350, 3500, 3.78880649805069e-05),

    },
    "tai_yang": {'li_zhi': [43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379,
                            414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939, 993,
                            1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668],
                 'xs': 750,
                 'xyz': (5250, 5000, 0.000025)
                 },

}
FILE_PATH = r'{}'.format(path.join(getenv("APPDATA", ""), "count_buff", "data.json"))
DEFAULT_DATA = {
    'ty_lv': 37,
    'ty_intellect': 0,
    'ty3_lv': 3,
    'buff_amount': 0,
    'out_intellect': 0,
    'out_lv': 21,
    'out_medal': 50,
    'out_earp': 175,
    'out_guild': 80,
    'in_intellect': 0,
    'in_lv': 35,
    'halo_amount': 0,
    'pet_amount': 0,
    'jade_amount': 0,
    'fixed_attack': 0,
    'fixed_intellect': 0,
    'percentage_attack': [],
    'percentage_intellect': [],
    'ty_fixed': 0,
    'ty_percentage': [],
    'cp_arms': True,
    'nai_ba_guardian': 0,
    'nai_ba_ssp': 0,
    "ty3_true": True,
    "c_attack": 3350,
    "c_intellect": 24500,
    "lv_01": 1,
    "lv_02": 1,
    "lv_03": 1,
    "lv_04": 1,
    "buff_wz": 0
}
#########
career = 'nai_ma'

save_data = {
    "nai_ma": [{
        "name": "奶妈",
        "data": DEFAULT_DATA.copy()
    }],

    "nai_ba": [{
        "name": "奶爸",
        "data": DEFAULT_DATA.copy()
    }
    ],
    "nai_luo": [{
        "name": "奶萝",
        "data": DEFAULT_DATA.copy()
    }],
    "nai_gong": [{
        "name": "奶弓",
        "data": DEFAULT_DATA.copy()
    }],
    "record": {
        "nai_ma": 0,
        "nai_ba": 0,
        "nai_luo": 0,
        "nai_gong": 0
    },
    "career": career
}
baseline_data = DEFAULT_DATA.copy()


#############################
# 核心计算函数
def count_buff(buff_amount: int, intellect: int, xs: int, xyz: tuple, cp_arms: bool,
               arm=1.08):  # 这个arm参数仅用于临时修正奶爸的站街武器BUG
    """

    :param buff_amount: 增益量
    :param intellect: 四维
    :param xs: 系数
    :param xyz: x,y,z
    :param cp_arms: cp武器
    :param arm:
    :return: 函数
    """
    x, y, z = xyz

    def count(fixed, bfb: list, basic_attack) -> int:
        """

        :param fixed: 固定加成
        :param bfb: 百分比加成
        :param basic_attack: 基础数值
        :return:
        """

        old_buff = ((basic_attack + fixed) * ((intellect / xs) + 1))
        for n in bfb:
            old_buff *= (1 + n / 100)
        new_buff = basic_attack * ((intellect + x) / xs + 1) * (buff_amount + y) * z if buff_amount != 0 else 0
        buff_ = (old_buff + new_buff) * (arm if cp_arms else 1)
        return round(buff_)

    return count


def diff_dict(dict1, dict2):
    diff = {}
    for key in dict1:
        if isinstance(dict1[key], dict):
            diff[key] = diff_dict(dict1[key], dict2[key])  # 递归
        else:
            diff[key] = dict2[key] - dict1[key]
            if isinstance(diff[key], float):
                diff[key] = round(diff[key], 2)
    return diff


def value_to_str(data):
    if isinstance(data, dict):
        for key in data:
            data[key] = value_to_str(data[key])
    else:
        data = str(data)
    return data


# buff最顶层
def buff(cr: str, data: dict):
    power = {'zj': count_zj_buff(cr, data),
             'jt': count_jt_buff(cr, data),
             'ty': count_ty(data),
             }
    power['ty3'] = round(power['ty'] * ((1.08 if data['ty3_true'] else 1.23) + data['ty3_lv'] * 0.01))
    return power


def count_zj_buff(cr: str, data) -> dict:
    arm = 1.008 if cr == 'nai_ba' else 1.08  # 奶爸武器bug
    count = count_buff(
        int(data['buff_amount'] * (1 + data['halo_amount'] / 100 + data['pet_amount'] / 100 + data['buff_wz'] / 100)),
        data['out_intellect'],
        BUFF_BASE[cr]['xs'],
        BUFF_BASE[cr]['xyz'],
        data['cp_arms'],
        arm  # 奶爸武器bug
    )
    return {
        'sg': count(
            data['fixed_attack'],
            data['percentage_attack'],
            BUFF_BASE[cr]['san_gong'][data['out_lv'] - 1],

        ),

        'lz': count(
            data['fixed_intellect'],
            data['percentage_intellect'],
            BUFF_BASE[cr]['li_zhi'][data['out_lv'] - 1],
        )}


# 计算进图buff
def count_jt_buff(cr, data) -> dict:
    count = count_buff(
        int(data['buff_amount'] * (
                1 + data['halo_amount'] / 100 + data['pet_amount'] / 100 + data['jade_amount'] / 100 + data['buff_wz'] / 100)),
        data['in_intellect'],
        BUFF_BASE[cr]['xs'],
        BUFF_BASE[cr]['xyz'],
        data['cp_arms']
    )
    return {
        'sg': count(
            data['fixed_attack'],
            data['percentage_attack'],
            BUFF_BASE[cr]['san_gong'][data['in_lv'] - 1],
        ),
        'lz': count(
            data['fixed_intellect'],
            data['percentage_intellect'],
            BUFF_BASE[cr]['li_zhi'][data['in_lv'] - 1],
        )}


# 计算太阳
def count_ty(data) -> int:
    count = count_buff(
        int(data['buff_amount'] * (
                1 + data['halo_amount'] / 100 + data['pet_amount'] / 100 + data['jade_amount'] / 100 + data['buff_wz'] / 100)),
        data['ty_intellect'],
        BUFF_BASE['tai_yang']['xs'],
        BUFF_BASE['tai_yang']['xyz'],
        False)
    return count(data['ty_fixed'],
                 data['ty_percentage'],
                 BUFF_BASE['tai_yang']['li_zhi'][data['ty_lv'] - 1],
                 )


def gap_set(gap):
    if isinstance(gap, dict):
        for key in gap:
            gap[key] = gap_set(gap[key])
    else:
        gap = f"<font color='#FF8C00'>+{gap}<font>" if gap >= 0 else f"<font color='#f40c0c'>{gap}<font>"
    return gap


def count_magnification(data, ty3, attribute, c_attack, c_intellect):
    attack, intellect = data['sg'], data['lz']

    return {
        "resident": round((1 + attack / c_attack) * (1 + intellect / (c_intellect + 250)) * attribute, 2),
        "burst": round((1 + attack / c_attack) * (1 + (intellect + ty3) / (c_intellect + 250)) * attribute, 2)
    }


def nai_ma_skill(skill, lv):
    if skill == '15':
        return \
            [0, 86, 90, 94, 98, 102, 107, 112, 117, 123, 129, 135, 141, 147, 154, 161, 169, 177, 185, 193, 201, 210, 219, 229, 238, 248, 258, 269, 279, 290,
             301,
             313, 325, 337, 349, 361, 375, 388, 401, 415, 429, 443, 457, 473, 487, 503, 519, 535, 551, 567, 584, 598, 614, 630, 646, 662, 677, 693, 709, 725,
             741,
             756, 772, 788, 804, 820, 835, 851, 867, 883, 899][70 if lv > 70 else lv]
    elif skill == '50':
        return 14 + lv // 2 * 23 + ((lv - 1) // 2) * 22
    elif skill == '75':
        return 140 + lv * 10
    elif skill == '95':
        return 150 + lv * 10


def nai_luo_skill(skill, lv):
    if skill == '15':
        return \
            [0, 69, 73, 77, 81, 85, 90, 95, 100, 106, 112, 118, 124, 130, 137, 144, 152, 160, 168, 176, 184, 193, 202, 212, 221, 231, 241, 252, 262, 273, 284,
             296, 308, 320, 332, 344, 358, 371, 384, 398, 412, 426, 440, 456, 470, 486, 502, 518, 534, 550, 567, 581, 597, 613, 629, 645, 660, 676, 692, 708,
             724, 739, 755, 771, 787, 803, 818, 834, 850, 866, 882][70 if lv > 70 else lv]
    elif skill == '50':
        return 14 + lv // 2 * 23 + ((lv - 1) // 2) * 22
    elif skill == '75':
        return 140 + lv * 10
    elif skill == '95':
        return 150 + lv * 10


def nai_gong_skill(skill, lv):
    if skill == '15':
        return \
            [0, 276, 280, 284, 288, 292, 297, 302, 307, 313, 319, 325, 331, 337, 344, 351, 359, 367, 375, 383, 391, 400, 409, 419, 428, 438, 448, 459, 469, 480,
             491, 503, 515, 527, 539, 551,
             565, 578, 591, 605, 619, 633, 647, 663, 677, 693, 709, 725, 741, 757, 774, 788, 804, 820, 836, 852, 867, 883, 899, 915, 931, 946, 962, 978, 994,
             1010, 1025, 1041, 1057, 1073, 1089][70 if lv > 70 else lv]
    elif skill == '50':
        return 14 + lv // 2 * 23 + ((lv - 1) // 2) * 22
    elif skill == '75':
        return 140 + lv * 10
    elif skill == '95':
        return 150 + lv * 10


def button_count_clicked():
    input_data = UI.get_values()

    # 下面是 向下取整,还是四舍五入 有待研究
    if career == 'nai_ma':
        now_intellect = nai_ma_skill('15', input_data['lv_01']) + nai_ma_skill('75', input_data['lv_03']) + nai_ma_skill('95', input_data['lv_04'])
        base_intellect = nai_ma_skill('15', baseline_data['lv_01']) + nai_ma_skill('75', baseline_data['lv_03']) + nai_ma_skill('95', baseline_data['lv_04'])
        intellect = now_intellect - base_intellect + input_data["add"]
        input_data['out_intellect'] += intellect
        lv1 = 14 + input_data['lv_02'] // 2 * 23 + ((input_data['lv_02'] - 1) // 2) * 22
        lv2 = 14 + baseline_data['lv_02'] // 2 * 23 + ((baseline_data['lv_02'] - 1) // 2) * 22
        intellect += (lv1 - lv2)
        input_data['in_intellect'] += intellect
        input_data['ty_intellect'] += intellect
        #############################################
        now = buff(career, input_data)
        base = buff(career, baseline_data)
        now['z_jt'] = {k: round(v * 1.15) for k, v in now['jt'].items()}
        base['z_jt'] = {k: round(v * 1.15) for k, v in base['jt'].items()}
        now.update(
            count_magnification(now['z_jt'], now['ty3'], 1.141, input_data['c_attack'], input_data['c_intellect']))
        base.update(
            count_magnification(base['z_jt'], base['ty3'], 1.141, input_data['c_attack'], input_data['c_intellect']))
        gap = diff_dict(base, now)
        UI.set_show_text(value_to_str(now), gap_set(gap))
    elif career == 'nai_luo':
        now_intellect = nai_luo_skill('15', input_data['lv_01']) + nai_luo_skill('75', input_data['lv_03']) + nai_luo_skill('95', input_data['lv_04'])
        base_intellect = nai_luo_skill('15', baseline_data['lv_01']) + nai_luo_skill('75', baseline_data['lv_03']) + nai_luo_skill('95', baseline_data['lv_04'])
        intellect = now_intellect - base_intellect + input_data["add"]
        input_data['out_intellect'] += intellect
        lv1 = 14 + input_data['lv_02'] // 2 * 23 + ((input_data['lv_02'] - 1) // 2) * 22
        lv2 = 14 + baseline_data['lv_02'] // 2 * 23 + ((baseline_data['lv_02'] - 1) // 2) * 22
        intellect += (lv1 - lv2)
        input_data['in_intellect'] += intellect
        input_data['ty_intellect'] += intellect
        #############################################

        now = buff(career, input_data)
        base = buff(career, baseline_data)
        now['z_jt'] = {k: round(v * 1.25) for k, v in now['jt'].items()}
        now['p_jt'] = {k: round(v * 1.4375) for k, v in now['jt'].items()}
        base['z_jt'] = {k: round(v * 1.25) for k, v in base['jt'].items()}
        base['p_jt'] = {k: round(v * 1.4375) for k, v in base['jt'].items()}
        now.update(
            count_magnification(now['p_jt'], now['ty3'], 1.141, input_data['c_attack'], input_data['c_intellect']))
        base.update(
            count_magnification(base['p_jt'], base['ty3'], 1.141, input_data['c_attack'], input_data['c_intellect']))
        gap = diff_dict(base, now)
        UI.set_show_text(value_to_str(now), gap_set(gap))
    elif career == 'nai_ba':

        now = buff(career, input_data)
        base = buff(career, baseline_data)
        _ = baseline_data.copy()
        _['in_intellect'] = _['in_intellect'] + _['nai_ba_guardian'] + _['nai_ba_ssp'] * 24
        input_data['in_intellect'] = input_data['in_intellect'] + input_data['nai_ba_guardian'] + input_data[
            'nai_ba_ssp'] * 24
        now['z_jt'] = count_jt_buff(career, input_data)
        base['z_jt'] = count_jt_buff(career, _)

        now.update(
            count_magnification(now['z_jt'], now['ty3'], 1.141, input_data['c_attack'], input_data['c_intellect']))
        base.update(
            count_magnification(base['z_jt'], base['ty3'], 1.141, input_data['c_attack'], input_data['c_intellect']))

        gap = diff_dict(base, now)
        UI.set_show_text(value_to_str(now), gap_set(gap))
    elif career == 'nai_gong':

        now_intellect = nai_gong_skill('15', input_data['lv_01']) + nai_gong_skill('75', input_data['lv_03']) + nai_gong_skill('95', input_data['lv_04'])
        base_intellect = nai_gong_skill('15', baseline_data['lv_01']) + nai_gong_skill('75', baseline_data['lv_03']) + nai_gong_skill('95',
                                                                                                                                      baseline_data['lv_04'])
        intellect = now_intellect - base_intellect + input_data["add"]
        input_data['out_intellect'] += intellect
        lv1 = 14 + input_data['lv_02'] // 2 * 23 + ((input_data['lv_02'] - 1) // 2) * 22
        lv2 = 14 + baseline_data['lv_02'] // 2 * 23 + ((baseline_data['lv_02'] - 1) // 2) * 22
        intellect += (lv1 - lv2)
        input_data['in_intellect'] += intellect
        input_data['ty_intellect'] += intellect
        #############################################

        now = buff(career, input_data)
        base = buff(career, baseline_data)
        now['z_jt'] = {k: round(v * 1.1) for k, v in now['jt'].items()}
        base['z_jt'] = {k: round(v * 1.1) for k, v in base['jt'].items()}
        now.update(
            count_magnification(now['z_jt'], now['ty3'], 1.174, input_data['c_attack'], input_data['c_intellect']))
        base.update(
            count_magnification(base['z_jt'], base['ty3'], 1.174, input_data['c_attack'], input_data['c_intellect']))
        gap = diff_dict(base, now)
        UI.set_show_text(value_to_str(now), gap_set(gap))


def is_contrast():
    global baseline_data
    data = UI.get_values()

    if data['add'] != 0 and QMessageBox.question(widget, "快捷计算", "是否将智力/精神,加到面板内？", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
        data['in_intellect'] += data['add']
        data['ty_intellect'] += data['add']
        data['out_intellect'] += data['add']
    UI.add.setText('')
    baseline_data = data.copy()
    UI.set_placeholder_texts(baseline_data)
    button_count_clicked()
    UI.clear_show_hold_text()


def is_save():
    global save_data
    input_data = UI.get_values()
    input_data.pop('add', 1)
    print(career)
    db = save_data[career][save_data['record'][career]]['data']
    for k, v in input_data.items():
        if db[k] != v:
            print(k, db[k], v, )
            if QMessageBox.question(widget, "消息框标题", "数据未保存,是否保存数据？",
                                    QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                cfg_id = save_data['record'][career]
                save_data[career][cfg_id]['data'] = input_data


def save(update=False):
    global save_data

    if not path.exists(path.dirname(FILE_PATH)):
        makedirs(path.dirname(FILE_PATH))
    if update:
        cfg_id = save_data['record'][career]
        save_data[career][cfg_id]['data'] = UI.get_values()
        button_count_clicked()
        is_contrast()
    with open(FILE_PATH, "w+") as f:
        json.dump(save_data, f)


def load_data():
    global save_data, career
    # 首次运行创建文件夹及文件步骤写到save_data里不要写在这.否则可能会报毒
    try:
        with open(FILE_PATH, "r") as f:
            save_data = json.load(f)
            _ = ('nai_ma', 'nai_ba', 'nai_luo', "nai_gong")
            for cr in _:
                if isinstance(save_data[cr], dict):
                    data = []
                    for v in save_data[cr].values():
                        data.append(v)

                    save_data[cr] = data
                    save_data['record'][cr] = 0
    except:
        pass  # 如果读取不到或者读取错则什么都不做,用默认数据]
    career = save_data['career']
    career_button_clicked(career)
    update_config()
    if career == 'nai_ma':
        UI.naima_button.click()
    elif career == 'nai_ba':
        UI.naiba_button.click()
    elif career == 'nai_luo':
        UI.nailuo_button.click()
    elif career == 'nai_gong':
        UI.naigong_button.click()
    button_count_clicked()
    is_contrast()


def config_clicked(config_id):
    global save_data
    save_data['record'][career] = config_id
    data = save_data[career][config_id]['data']
    UI.set_values(data)
    UI.button_save.setText(f'保存({save_data[career][config_id]["name"]})')
    button_count_clicked()
    is_contrast()


def update_config():
    UI.config_list.clear()
    select_id = save_data["record"][career]

    for cfg_id, cfg in enumerate(save_data[career]):
        if select_id == cfg_id:
            config_clicked(select_id)
            UI.add_config(cfg['name'], True)

        else:
            UI.add_config(cfg['name'])


def add_config(select=False):
    name, ok = QInputDialog.getText(widget, "", "请输入配置名")
    if ok:
        if name == "":
            QMessageBox.critical(widget, '错误', '配置名不能是空')
            return
        global save_data
        save_data[career].append({
            'name': name,
            'data': DEFAULT_DATA.copy()
        })
        UI.add_config(name, select)
        config_clicked(len(save_data[career]) - 1)
        save()


def set_config_name(item):
    global save_data
    cfg_id = UI.config_list.row(item)
    save_data[career][cfg_id]['name'] = item.text()
    save()


def del_config():
    global save_data
    if len(save_data[career]) == 1:
        QMessageBox.critical(widget, '错误', '至少保留一个吧！')
    elif QMessageBox.question(widget, "消息框标题", "确实删除吗？", QMessageBox.Yes | QMessageBox.No,
                              QMessageBox.Yes) == QMessageBox.Yes:

        items = UI.config_list.selectedItems()
        row = 0
        for im in items:
            row = UI.config_list.row(im)
            UI.config_list.takeItem(row)
            UI.config_list.update()
            UI.config_list.repaint()
            del save_data[career][row]
        row = 0 if (row - 1) < 0 else row - 1
        item = UI.config_list.item(row)
        item.setSelected(True)
        config_clicked(row)

        UI.config_list.update()
        UI.config_list.repaint()
        save(False)


# 是否保存数据


def career_button_clicked(career_name):
    global career, save_data
    career = career_name
    save_data["career"] = career_name
    update_config()
    UI.left_widget.update()
    if career == 'nai_ma':
        widget.setWindowIcon(QIcon(":/png/84.PNG"))
    elif career == 'nai_ba':
        widget.setWindowIcon(QIcon(":/png/111.PNG"))
    elif career == 'nai_luo':
        widget.setWindowIcon(QIcon(":/png/719.PNG"))
    elif career == 'nai_gong':
        widget.setWindowIcon(QIcon(":/png/14.PNG"))


def close_windows():
    save()
    QCoreApplication.instance().quit()


def window_top():
    if bool(widget.windowHandle().flags() & Qt.WindowStaysOnTopHint):
        widget.window_top(False)
        UI.button_top.setStyleSheet("")
    else:
        widget.window_top(True)
        UI.button_top.setStyleSheet("background:rgb(212, 218, 230);")


def add_button():
    if career == 'nai_ba':
        return
    lv_min = int(UI.add_1.text())
    lv_max = int(UI.add_2.text())
    lv_count = int(UI.add_3.text())
    # #########
    if lv_min <= 15 <= lv_max:
        UI.set_value('lv_01', UI.get_value('lv_01') + lv_count)
    if lv_min <= 30 <= lv_max:
        lv1 = UI.get_value('out_lv') + lv_count
        UI.set_value('out_lv', lv1 if lv1 < 41 else 40)
        lv2 = UI.get_value('in_lv') + lv_count
        UI.set_value('in_lv', lv2 if lv2 < 41 else 40)
    if lv_min <= 50 <= lv_max:
        UI.set_value('lv_02', UI.get_value('lv_02') + lv_count)
        lv1 = UI.get_value('ty_lv') + lv_count
        UI.set_value('ty_lv', lv1 if lv1 < 41 else 40)
    if lv_min <= 75 <= lv_max:
        UI.set_value('lv_03', UI.get_value('lv_03') + lv_count)
    if lv_min <= 95 <= lv_max:
        UI.set_value('lv_04', UI.get_value('lv_04') + lv_count)
    if lv_min <= 100 <= lv_max:
        UI.set_value('ty3_lv', UI.get_value('ty3_lv') + lv_count)
    button_count_clicked()


# 开始,绑定按钮函数
def start():
    load_data()
    UI.button_lv_add.clicked.connect(add_button)
    # UI.button_js.clicked.connect(button_count_clicked)
    UI.button_jc.clicked.connect(is_contrast)
    UI.button_add.clicked.connect(lambda: add_config(True))
    UI.button_del.clicked.connect(del_config)
    UI.button_save.clicked.connect(lambda: save(True))
    UI.button_min.clicked.connect(lambda: widget.showMinimized())
    UI.button_top.clicked.connect(window_top)
    UI.button_close.clicked.connect(close_windows)
    UI.config_list.itemClicked.connect(lambda _: config_clicked(UI.config_list.row(_)))
    # UI.config_list.itemChanged.connect(lambda s: set_config_name(s))
    UI.nailuo_button.clicked.connect(lambda: career_button_clicked('nai_luo'))
    UI.naima_button.clicked.connect(lambda: career_button_clicked('nai_ma'))
    UI.naiba_button.clicked.connect(lambda: career_button_clicked('nai_ba'))
    UI.naigong_button.clicked.connect(lambda: career_button_clicked('nai_gong'))
    for k, v in UI.input_data.items():
        if isinstance(v, QLineEdit):
            v.textEdited.connect(button_count_clicked)
    UI.radioButton.clicked.connect(button_count_clicked)
    UI.radioButton_2.clicked.connect(button_count_clicked)
    UI.cp_arm.clicked.connect(button_count_clicked)
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(10)  # 范围
    effect.setOffset(0, 0)  # 横纵,偏移量
    effect.setColor(Qt.black)  # 颜色
    UI.widget_1.setGraphicsEffect(effect)


if __name__ == '__main__':
    app = QApplication(argv)

    # ui初始化
    widget = RoundedWindow()
    UI = BuffUI()
    UI.setupUi(widget)
    UI.init()
    ##########
    widget.show()
    widget.setWindowTitle(' 奶量计算器')
    widget.setStyleSheet("color: rgb(0, 0, 0);\n")
    ##############
    start()
    app.exec_()
