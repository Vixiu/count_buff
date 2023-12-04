import json
from os import getenv, path, makedirs
from sys import argv
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QCoreApplication, QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect, QHBoxLayout, QWidget, QInputDialog, QMessageBox, \
    QLineEdit

from UI import Ui_widget
from Widget import RoundedWindow
from PyQt5.QtWidgets import QPushButton

from UIData import UIData

BUFF_BASE = {
    'nai_ma': {
        'san_gong': [39, 41, 43, 44, 45, 47, 49, 50, 52, 53, 54, 56, 58, 59, 61, 62,
                     63, 65, 67, 69, 70, 71, 73, 75, 77, 79, 80, 81, 83, 85, 86, 88,
                     89, 90, 92, 94, 95, 97, 98, 100],
        'li_zhi': [154, 164, 176, 186, 197, 206, 216, 227, 237, 249, 259, 269, 280, 290,
                   302, 311, 321, 332, 342, 353, 363, 374, 385, 395, 406, 415, 425, 437,
                   447, 458, 468, 478, 489, 500, 511, 520, 530, 541, 551, 563],
        'xs': 665,
        'xyz': (4350, 3500, 3.7886202335357666e-05),
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
        'xyz': (4350, 3500, 3.7886202335357666e-05),

    },
    'nai_luo': {
        'san_gong': [34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54,
                     55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76,
                     77, 78, 80, 81, 82, 84, 85, 87],
        'li_zhi': [131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247,
                   256, 264, 273, 282, 291, 300, 309, 318, 327, 336, 345, 353, 362, 371,
                   380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478],
        'xs': 665,
        'xyz': (4350, 3500, 3.7886202335357666e-05),

    },
    "tai_yang": {'li_zhi': [43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379,
                            414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939, 993,
                            1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668],
                 'xs': 750,
                 'xyz': (5250, 5000, 0.000025)
                 },

}
FILE_PATH = r'{}'.format(path.join(getenv("APPDATA", ""), "count_buff", "data.json"))
UI = Ui_widget()
now_career = 'nai_ma'
DATA = UIData()
data_base = {
    'ty_lv': 37,
    'ty_intellect': 0,
    'ty3_lv': 3,
    'buff_amount': 0,
    'out_intellect': 0,
    'out_lv': 1,
    'out_medal': 50,
    'out_earp': 175,
    'out_passive': 554,
    'out_guild': 80,
    'in_intellect': 0,
    'in_lv': 21,
    'halo_amount': 0,
    'pet_amount': 0,
    'jade_amount': 0,
    'fixed_attack': 0,
    'fixed_intellect': 0,
    'percentage_attack': [],
    'percentage_intellect': [],
    'ty_fixed': 0,
    'ty_percentage': [],
    'cp_arm': True,
    'nai_ba_guardian': 0,
    'nai_ba_ssp': 0,
}
save_data = {
    "nai_ma": {
        "pz_1": {
            "name": "默认配置",
            "data": data_base.copy()
        },

    },
    "nai_ba": {
        "pz_1": {
            "name": "默认配置",
            "data": data_base.copy()
        },

    },
    "nai_luo": {
        "pz_1": {
            "name": "默认配置",
            "data": data_base.copy()
        },

    },
    "nai_gong": {
        "pz_1": {
            "name": "默认配置",
            "data": data_base.copy()
        },

    },
    "record": {
        "nai_ma": 'pz_1',
        "nai_ba": 'pz_1',
        "nai_luo": 'pz_1',
        "nai_gong": 'pz_1'
    },
    "career": now_career
}


# buff最顶层
def buff(data_now):
    cr = now_career
    data_now['in_intellect'] += data_now["add"]
    data_now['out_intellect'] += data_now["add"]
    data_now['ty_intellect'] += data_now["add"]
    now = {'zj': count_zj_buff(cr, data_now),
           'jt': count_jt_buff(cr, data_now),
           'ty': count_ty(data_now),
           }
    base = {
        'zj': count_zj_buff(cr, data_base),
        'jt': count_jt_buff(cr, data_base),
        'ty': count_ty(data_base)
    }
    now.update(count_ty3(now['ty'], data_now['ty3_lv']))
    base.update(count_ty3(base['ty'], data_base['ty3_lv']))
    return now, base


# 计算三觉力智
def count_ty3(intellect, lv):
    return {
        'san_one': round(intellect * (1.08 + lv * 0.01)),
        'san_two': round(intellect * (1.23 + lv * 0.01)),
    }


# 递归将字典的值转换为字符串
def value_to_str(data):
    if isinstance(data, dict):
        for key in data:
            data[key] = value_to_str(data[key])
    else:
        data = str(data)
    return data


# 递归设置差距文本样式
def gap_set(gap):
    if isinstance(gap, dict):
        for key in gap:
            gap[key] = gap_set(gap[key])
    else:
        gap = "<font color='{}'>{:+d}<font>".format('#21f805' if gap >= 0 else '#f40c0c', gap)
    return gap


# 设置显示数据
def current(data, gap):
    UI.buff_sg.setText(data['zj']['sg'])
    UI.buff_lz.setText(data['zj']['lz'])
    UI.buff_sg_cj.setText(gap['zj']['sg'])
    UI.buff_lz_cj.setText(gap['zj']['lz'])
    UI.yijue_lz.setText(data['ty'])
    UI.yijue_cj.setText(gap['ty'])
    UI.sanjue_lz_1.setText(data['san_one'])
    UI.sanjue_lz_1_cj.setText(gap['san_one'])
    UI.sanjue_lz_2.setText(data['san_two'])
    UI.sanjue_lz_2_cj.setText(gap['san_two'])
    UI.b1_sg.setText(data['jt']['sg'])
    UI.b1_lz.setText(data['jt']['lz'])
    UI.b1_sg_cj.setText(gap['jt']['sg'])
    UI.b1_lz_cj.setText(gap['jt']['lz'])
    UI.b2_sg.setText(data['z_jt']['sg'])
    UI.b2_lz.setText(data['z_jt']['lz'])
    UI.b2_sg_cj.setText(gap['z_jt']['sg'])
    UI.b2_lz_cj.setText(gap['z_jt']['lz'])


# 设置奶妈计算结果
def set_naima(data, gap):
    current(data, gap)


# 设置奶罗计算结果
def set_nailuo(data, gap):
    current(data, gap)
    UI.b3_sg.setText(data['p_jt']['sg'])
    UI.b3_lz.setText(data['p_jt']['lz'])
    UI.b3_lz_cj.setText(gap['p_jt']['lz'])
    UI.b3_sg_cj.setText(gap['p_jt']['sg'])


# 设置奶爸计算结果
def set_naiba(data, gap):
    current(data, gap)


# 设置奶公计算结果
def set_naigong(data, gap):
    current(data, gap)


# 清除所有显示内容
def clear():
    clear_text()
    clear_cj()
    UI.nailuo_button.setStyleSheet('')
    UI.naiba_button.setStyleSheet('')
    UI.naima_button.setStyleSheet('')
    UI.naigong_button.setStyleSheet('')


# 设置奶妈显示文本
def naima_setting():
    global now_career

    is_save()

    clear()
    UI.tabWidget.removeTab(2)
    main_window.setWindowIcon(QIcon(":/png/84.PNG"))
    UI.label_6.setText('智力加减:')
    UI.label_3.setText('智力:')
    UI.label_17.setText('智力:')
    UI.label_15.setText('智力:')
    now_career = 'nai_ma'
    UI.naima_button.setStyleSheet('border:0px; border-radius: 0px;'
                                  ' padding-top:8px;'
                                  'padding-bottom:8px;'
                                  'border-left: 5px solid rgb(5, 229, 254);'
                                  'background-color:rgb(217, 217, 217);')
    UI.yijue.setTitle('圣光天启')
    UI.sanjue.setTitle('祈愿·天使赞歌')
    UI.yijue_icon.setPixmap(QtGui.QPixmap(":/png/23.PNG"))
    UI.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/350.PNG"))
    UI.b0.setTitle('勇气祝福')
    UI.label_35.setPixmap(QtGui.QPixmap(":/png/84.PNG"))
    UI.b1.setTitle('勇气祝福')
    UI.label_30.setPixmap(QtGui.QPixmap(":/png/84.PNG"))
    UI.b2.setTitle('勇气+颂歌')
    UI.b3.hide()

    pz_setting(now_career)
    pz_clicked(save_data['record'][now_career])

    button_count_clicked()
    is_contrast()

# 设置奶罗显示文本
def nailuo_setting():
    global now_career
    is_save()
    clear()
    UI.tabWidget.removeTab(2)
    main_window.setWindowIcon(QIcon(":/png/719.PNG"))
    UI.label_6.setText('智力加减:')
    UI.label_3.setText('智力:')
    UI.label_17.setText('智力:')
    UI.label_15.setText('智力:')
    now_career = 'nai_luo'
    UI.yijue.setTitle('开幕！人偶剧场')
    UI.sanjue.setTitle('终幕！人偶剧场')
    UI.nailuo_button.setStyleSheet('border:0px; border-radius: 0px;'
                                   ' padding-top:8px;'
                                   'padding-bottom:8px;'
                                   'border-left: 5px solid rgb(5, 229, 254);'
                                   'background-color:rgb(217, 217, 217);')
    UI.yijue_icon.setPixmap(QtGui.QPixmap(":/png/757.PNG"))
    UI.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/838.PNG"))
    UI.b0.setTitle('禁忌诅咒')
    UI.b1.setTitle('禁忌诅咒')

    UI.label_35.setPixmap(QtGui.QPixmap(":/png/719.PNG"))
    UI.label_30.setPixmap(QtGui.QPixmap(":/png/719.PNG"))
    UI.b2.setTitle('禁忌诅咒+疯狂召唤')
    UI.b3.show()
    pz_setting(now_career)
    pz_clicked(save_data['record'][now_career])
    button_count_clicked()
    is_contrast()

# 设置奶爸显示文本
def naiba_setting():
    global now_career
    is_save()
    clear()
    UI.tabWidget.insertTab(2, UI.tab3, '奶爸二觉')
    main_window.setWindowIcon(QIcon(":/png/111.PNG"))
    UI.label_6.setText('体精加减:')
    UI.label_3.setText('体精:')
    UI.label_17.setText('体精:')
    UI.label_15.setText('体精:')
    now_career = 'nai_ba'
    UI.naiba_button.setStyleSheet('border:0px; border-radius: 0px;'
                                  ' padding-top:8px;'
                                  'padding-bottom:8px;'
                                  'border-left: 5px solid rgb(5, 229, 254);'
                                  'background-color:rgb(217, 217, 217);')
    UI.yijue.setTitle('天启之珠')
    UI.sanjue.setTitle('生命礼赞:神威')
    UI.yijue_icon.setPixmap(QtGui.QPixmap(":/png/158.PNG"))
    UI.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/548.PNG"))
    UI.b0.setTitle('荣誉祝福')
    UI.label_35.setPixmap(QtGui.QPixmap(":/png/111.PNG"))
    UI.b1.setTitle('荣誉祝福')
    UI.label_30.setPixmap(QtGui.QPixmap(":/png/111.PNG"))
    UI.b2.setTitle('守护+荣誉祝福(24层)')
    UI.b3.hide()
    pz_setting(now_career)
    pz_clicked(save_data['record'][now_career])
    button_count_clicked()
    is_contrast()

# 设置奶公显示文本
def naigong_setting():
    global now_career
    is_save()
    clear()
    UI.tabWidget.removeTab(2)
    main_window.setWindowIcon(QIcon(":/png/14.PNG"))
    UI.label_6.setText('精神加减:')
    UI.label_3.setText('精神:')
    UI.label_17.setText('精神:')
    UI.label_15.setText('精神:')
    UI.naigong_button.setStyleSheet('border:0px; border-radius: 0px;'
                                    ' padding-top:8px;'
                                    'padding-bottom:8px;'
                                    'border-left: 5px solid rgb(5, 229, 254);'
                                    'background-color:rgb(217, 217, 217);')
    UI.yijue.setTitle('梦想的舞台')
    UI.sanjue.setTitle('终曲:霓虹蝶梦')
    UI.yijue_icon.setPixmap(QtGui.QPixmap(":/png/88.PNG"))
    UI.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/34.PNG"))
    UI.b0.setTitle('可爱节拍')
    UI.label_35.setPixmap(QtGui.QPixmap(":/png/14.PNG"))
    UI.b1.setTitle('可爱节拍')
    UI.label_30.setPixmap(QtGui.QPixmap(":/png/14.PNG"))
    UI.b2.setTitle('可爱节拍+燃情狂想曲')
    UI.b3.hide()
    now_career = 'nai_gong'
    pz_setting(now_career)
    pz_clicked(save_data['record'][now_career])
    button_count_clicked()
    is_contrast()

# 计算按钮绑定函数
@DATA
def button_count_clicked(data_now):
    now, base = buff(data_now)

    career = now_career
    # 下面是 向下取整,还是四舍五入 有待研究
    if career == 'nai_ma':
        now['z_jt'] = {k: round(v * 1.15) for k, v in now['jt'].items()}
        base['z_jt'] = {k: round(v * 1.15) for k, v in base['jt'].items()}
        gap = diff_dict(base, now)
        set_naima(value_to_str(now), gap_set(gap))
    elif career == 'nai_luo':
        now['z_jt'] = {k: round(v * 1.25) for k, v in now['jt'].items()}
        now['p_jt'] = {k: round(v * 1.4375) for k, v in now['jt'].items()}
        base['z_jt'] = {k: round(v * 1.25) for k, v in base['jt'].items()}
        base['p_jt'] = {k: round(v * 1.4375) for k, v in base['jt'].items()}
        gap = diff_dict(base, now)
        set_nailuo(value_to_str(now), gap_set(gap))
    elif career == 'nai_ba':
        _ = data_base.copy()
        _['in_intellect'] = _['in_intellect'] + data_base['nai_ba_guardian'] + data_base['nai_ba_ssp'] * 24
        data_now['in_intellect'] = data_now['in_intellect'] + data_now['nai_ba_guardian'] + data_now['nai_ba_ssp'] * 24
        now['z_jt'] = count_jt_buff(career, data_now)
        base['z_jt'] = count_jt_buff(career, _)
        #######################################

        gap = diff_dict(base, now)
        set_naiba(value_to_str(now), gap_set(gap))
    elif career == 'nai_gong':
        now['z_jt'] = {k: round(v * 1.1) for k, v in now['jt'].items()}
        base['z_jt'] = {k: round(v * 1.1) for k, v in base['jt'].items()}
        gap = diff_dict(base, now)
        set_naigong(value_to_str(now), gap_set(gap))


# 计算两个相同结构字典的差值
def diff_dict(dict1, dict2):
    diff = {}
    for key in dict1:
        if isinstance(dict1[key], dict):
            diff[key] = diff_dict(dict1[key], dict2[key])  # 递归
        else:
            diff[key] = dict2[key] - dict1[key]
    return diff


# 核心计算函数
def count_buff(buff_amount, intellect, xs, xyz: tuple, cp_arm: bool, arm=1.08):  # 这个arm参数仅用于临时修正奶爸的站街武器BUG
    """

    :param buff_amount: 增益量
    :param intellect: 四维
    :param xs: 系数
    :param xyz: x,y,z
    :param cp_arm: cp武器
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
        bf = (old_buff + new_buff) * (arm if cp_arm else 1)

        return round(bf)

    return count


# 计算站街buff
def count_zj_buff(cr: str, data) -> dict:
    arm = 1.008 if cr == 'nai_ba' else 1.08  # 奶爸武器bug
    count = count_buff(
        int(data['buff_amount'] * (1 + data['halo_amount'] / 100 + data['pet_amount'] / 100)),
        data['out_intellect'],
        BUFF_BASE[cr]['xs'],
        BUFF_BASE[cr]['xyz'],
        data['cp_arm'],
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
                1 + data['halo_amount'] / 100 + data['pet_amount'] / 100 + data['jade_amount'] / 100)),
        data['in_intellect'],
        BUFF_BASE[cr]['xs'],
        BUFF_BASE[cr]['xyz'],
        data['cp_arm']
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
                1 + data['halo_amount'] / 100 + data['pet_amount'] / 100 + data['jade_amount'] / 100)),
        data['ty_intellect'],
        BUFF_BASE['tai_yang']['xs'],
        BUFF_BASE['tai_yang']['xyz'],
        False)
    return count(data['ty_fixed'],
                 data['ty_percentage'],
                 BUFF_BASE['tai_yang']['li_zhi'][data['ty_lv'] - 1],
                 )


# 设置为基础数据
@DATA
def is_contrast(data_now):
    global data_base
    DATA.set_placeholder_texts(data_now)

    data_base = data_now.copy()

    button_count_clicked()
    clear_cj()


# 清除所有差距文本内容
def clear_cj():
    UI.buff_sg_cj.setText('')
    UI.buff_lz_cj.setText('')
    UI.b1_lz_cj.setText('')
    UI.b1_sg_cj.setText('')
    UI.b2_lz_cj.setText('')
    UI.b2_sg_cj.setText('')
    UI.b3_sg_cj.setText('')
    UI.b3_lz_cj.setText('')
    UI.yijue_cj.setText('')
    UI.sanjue_lz_1_cj.setText('')
    UI.sanjue_lz_2_cj.setText('')


# 清除所有buff数值文本内容
def clear_text():
    UI.buff_sg.setText('')
    UI.buff_lz.setText('')
    UI.b1_lz.setText('')
    UI.b1_sg.setText('')
    UI.b2_lz.setText('')
    UI.b2_sg.setText('')
    UI.b3_sg.setText('')
    UI.b3_lz.setText('')
    UI.yijue_lz.setText('')
    UI.sanjue_lz_1.setText('')
    UI.sanjue_lz_2.setText('')
    UI.add.setText('')


# 窗口关闭绑定函数
def close_windows():
    global save_data
    is_save()
    save_data['career'] = now_career
    if not path.exists(path.dirname(FILE_PATH)):
        makedirs(path.dirname(FILE_PATH))

    with open(FILE_PATH, "w+") as f:
        json.dump(save_data, f)

    QCoreApplication.instance().quit()


# 保存数据
@DATA
def save(data_now):
    if not path.exists(path.dirname(FILE_PATH)):
        makedirs(path.dirname(FILE_PATH))

    save_data[now_career][save_data['record'][now_career]]["data"] = data_now
    with open(FILE_PATH, "w+") as f:
        json.dump(save_data, f)
    is_contrast()


# 设置配置按钮
def pz_setting(cr):
    for i in reversed(range(h_layout.count())):
        h_layout.itemAt(i).widget().deleteLater()
    for k, v in save_data[cr].items():
        add_layout_widget(v['name'], k)


# 读取数据
def load():
    global save_data, now_career
    # 首次运行创建文件夹及文件步骤写到save_data里不要写在这.否则可能会报毒
    try:
        with open(FILE_PATH, "r") as f:
            save_data = json.load(f)
    except:
        pass  # 如果读取不到或者读取错则什么都不做,用默认数据
    _career = save_data['career']
    now_career = save_data['career']
    pz_setting(_career)
    pz_clicked(save_data['record'][_career], _career)
    if _career == 'nai_ma':
        naima_setting()
    elif _career == 'nai_ba':
        naiba_setting()
    elif _career == 'nai_luo':
        nailuo_setting()
    elif _career == 'nai_gong':
        naigong_setting()

    button_count_clicked()
    is_contrast()
    clear_cj()





# 最小化窗口
def minimize_window():
    main_window.showMinimized()


# 窗口置顶
def top_window():
    if bool(main_window.windowHandle().flags() & Qt.WindowStaysOnTopHint):
        main_window.window_top(False)
        UI.button_top.setStyleSheet("")
    else:
        main_window.window_top(True)
        UI.button_top.setStyleSheet("background:rgb(212, 218, 230);")


# 添加配置按钮
def add_layout_widget(name: str, btn_id: str):
    button = QPushButton(name)
    font = QtGui.QFont()
    font.setPointSize(13)
    button.setFont(font)
    button.setObjectName(btn_id)
    h_layout.addWidget(button)
    button.clicked.connect(lambda: pz_clicked(btn_id))


# 配置按钮绑定函数
def pz_clicked(pz_id, cr=None):
    cr = cr if cr else now_career
    datas = save_data[cr][pz_id]['data']
    clear_text()
    clear_cj()
    # 设置对应配置数据
    DATA.set_values(datas)
    '''        
    btn = scrollArea_widget.findChild(QPushButton, pz_id)
    btn.setStyleSheet("background:rgb(212, 218, 230);")

    '''
    # 设置对应按钮状态
    for btn in scrollArea_widget.findChildren(QWidget):
        if btn.objectName() == pz_id:
            btn.setStyleSheet("background:rgb(212, 218, 230);")
        else:
            btn.setStyleSheet("")
    save_data['record'][cr] = pz_id
    button_count_clicked()


# is_contrast()

# 增加配置按钮
def add_button():
    message, ok = QInputDialog.getText(main_window, "", "请输入配置名")
    if ok:
        keys = save_data[now_career].keys()
        ls = [int(k[3:]) for k in keys]
        pz_id = 1
        for i in range(len(ls) + 1):
            if i + 1 not in ls:
                pz_id = f'pz_{i + 1}'

                break

        add_layout_widget(message, pz_id)
        save_data[now_career][pz_id] = {
            'name': message,
            'data': data_base.copy()
        }

        pz_clicked(pz_id)
    save()


#  删除配置按钮
def del_button():
    if len(save_data[now_career]) == 1:
        QMessageBox.critical(main_window, '错误', '至少保留一个吧！')

    elif QMessageBox.question(main_window, "消息框标题", "确实删除吗？", QMessageBox.Yes | QMessageBox.No,
                              QMessageBox.Yes) == QMessageBox.Yes:
        pz_id = save_data['record'][now_career]
        for btn in scrollArea_widget.findChildren(QWidget):
            if btn.objectName() == pz_id:
                btn.deleteLater()
                del save_data[now_career][pz_id]
        pz_clicked(list(save_data[now_career].keys())[0])
        save()


# 是否保存数据
def is_save():
    data_now = DATA.get_values()
    db = save_data[now_career][save_data['record'][now_career]]['data'].copy()
    data_now.pop('add', 1)
    db.pop("add", 1)
    if not data_now == db:
        if QMessageBox.question(main_window, "消息框标题", "是否保存数据？",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            save()


def percent_sign_validator(input_box: QLineEdit):
    text = input_box.text().replace('。', '.').replace(' ', '').replace('，', ',').replace(',,', ',')
    for _ in text.split(','):
        try:
            if _:
                float(_)
        except ValueError:
            input_box.setText(text[:-1])
            return
    input_box.setText(text)


def float_validator(input_box: QLineEdit):
    text = input_box.text().replace('。', '.').replace(' ', '')
    try:
        float(text)
        input_box.setText(text)
    except ValueError:
        input_box.setText(text[:-1])


def lv_validator(input_box: QLineEdit):
    text = input_box.text().replace(' ', '')
    try:
        num = int(text)
        if num <= 40:
            input_box.setText(text)
        else:
            input_box.setText('40')
        if num == 0:
            input_box.setText('1')
    except ValueError:
        input_box.setText(text[:-1])


def lv_to(input_box: QLineEdit):
    lv_validator(input_box)
    zl_lv_text = input_box.text()
    if zl_lv_text:
        new_value = int(zl_lv_text) + 14
        if new_value <= 40:
            UI.jt_lv.setText(str(new_value))


def intellect_to():
    intellect = 0

    for le in ('out_medal', 'out_earp', 'out_passive', 'out_guild', 'out_intellect'):
        text = DATA.get_value(le)
        intellect += int(text)
    UI.jt_zhili.setText(str(intellect))
    UI.ty_zhili.setText(str(intellect))


def get_now_save_data():
    return save_data[now_career][save_data['record'][now_career]]['data']


# 开始,绑定按钮函数
def start():
    # 输入验证器
    int_validator = QRegExpValidator(QRegExp("^[0-9]*$"))
    # 验证器
    UI.buff_liang.setValidator(int_validator)
    UI.buff_gh.textEdited.connect(lambda: float_validator(UI.buff_gh))
    UI.lz_bfb.textEdited.connect(lambda: percent_sign_validator(UI.lz_bfb))
    UI.zl_lv.textEdited.connect(lambda: lv_to(UI.zl_lv))
    # 单击绑定
    UI.button_count.clicked.connect(button_count_clicked)
    UI.button_jc.clicked.connect(is_contrast)
    UI.button_close.clicked.connect(close_windows)
    UI.button_save.clicked.connect(save)
    UI.button_min.clicked.connect(minimize_window)
    UI.button_top.clicked.connect(top_window)
    UI.button_add.clicked.connect(add_button)
    UI.button_del.clicked.connect(del_button)
    # 职业按钮绑定
    UI.nailuo_button.clicked.connect(nailuo_setting)
    UI.naima_button.clicked.connect(naima_setting)
    UI.naiba_button.clicked.connect(naiba_setting)
    UI.naigong_button.clicked.connect(naigong_setting)
    # 文本变化绑定
    '''
    UI.zl_lv.textEdited.connect()
    UI.zj_xz.textEdited.connect(intellect_to)
    UI.zj_zhili.textEdited.connect(intellect_to)
    UI.zj_gh.textEdited.connect(intellect_to)
    UI.zj_eh.textEdited.connect(intellect_to)
    UI.zj_bd.textEdited.connect(intellect_to)
    UI.add.textEdited.connect(button_count_clicked)
    '''
    # 读取数据
    load()


if __name__ == '__main__':
    app = QApplication(argv)
    main_window = RoundedWindow()
    main_window.setStyleSheet("color: rgb(0, 0, 0);\n")
    main_window.setWindowTitle(' 奶量计算器')
    UI.setupUi(main_window)
    DATA.bind_input(UI)
    # ----这里后续可以移动到UI.py里去------------------------------
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(10)  # 范围
    effect.setOffset(0, 0)  # 横纵,偏移量
    effect.setColor(Qt.black)  # 颜色
    UI.widget_1.setGraphicsEffect(effect)
    ###
    scrollArea_widget = QWidget()
    scrollArea_widget.setStyleSheet("border-bottom: 1px solid #dadce0")
    h_layout = QHBoxLayout()
    scrollArea_widget.setLayout(h_layout)
    UI.scrollArea.setWidget(scrollArea_widget)
    UI.scrollArea.setStyleSheet("QScrollBar:vertical { height: 10px; }")
    # -----------------------------------------------------------------------
    start()
    main_window.show()
    app.exec_()
