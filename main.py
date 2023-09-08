
from os import getenv, path, makedirs
from sys import argv

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect

from UI import Ui_widget
from Widget import RoundedWindow
from ast import literal_eval
FILE_PATH = rf'{getenv("APPDATA")}\count_buff\data.json'
ui_home = Ui_widget()
BASIC_DATA = {
    'nai_ma': {
        'san_gong': [39, 41, 43, 44, 45, 47, 49, 50, 52, 53, 54, 56, 58, 59, 61, 62,
                     63, 65, 67, 69, 70, 71, 73, 75, 77, 79, 80, 81, 83, 85, 86, 88,
                     89, 90, 92, 94, 95, 97, 98, 100],
        'li_zhi': [154, 164, 176, 186, 197, 206, 216, 227, 237, 249, 259, 269, 280, 290,
                   302, 311, 321, 332, 342, 353, 363, 374, 385, 395, 406, 415, 425, 437,
                   447, 458, 468, 478, 489, 500, 511, 520, 530, 541, 551, 563],
        'xs': 665,
        'xyz': (4350, 3500, 0.00003788627),
        #       'xyz': (4345, 3500, 0.0000379),
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
        'xyz': (4350, 3500, 0.00003788627),

    },
    'nai_luo': {
        'san_gong': [34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54,
                     55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76,
                     77, 78, 80, 81, 82, 84, 85, 87],
        'li_zhi': [131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247,
                   256, 264, 273, 282, 291, 300, 309, 318, 327, 336, 345, 353, 362, 371,
                   380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478],
        'xs': 665,
        'xyz': (4350, 3500, 0.00003788627),

    },
    "tai_yang": {'li_zhi': [43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379,
                            414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939, 993,
                            1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668],
                 'xs': 750,
                 'xyz': (5250, 5000, 0.000025)
                 }
}
UI_DATA = {}
# 各项初始值
data_base = {
    'ty_lv': 37,
    'ty_intellect': 0,
    'buff_amount': 0,
    'out_intellect': 0,
    'out_lv': 1,

    'out_medal': 50,
    'out_earp': 175,
    'out_passive': 554,
    'out_guild': 80,

    'in_intellect': 0,
    'in_lv': 1,
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
    'career': 'nai_ma',

    'nai_ba_guardian': 0,
    'nai_ba_ssp': 0,

}


def input_validation(fn):
    # 因为还要对输入数据在进行一次判断，所以不在输入层面就进行效验
    def run_fn():
        data_now = {}

        def validation(text: str):
            if ',' in text:
                return False, [eval(i) for i in text.split(',') if i.isdigit()]
            elif text.startswith('+') or text.startswith('-'):
                return True, eval(text)
            elif text.isdigit() or ('.' in text and text.count('.') == 1):
                return False, eval(text)
            else:
                return False, text

        def input_data(k: str):
            text = UI_DATA.get(k).text().replace(" ", "").replace("，", ',').replace("。", '.')
            if text != '':
                bl, ve = validation(text)
                if type(ve) == str:
                    exception.append((k, ve))
                elif bl and k not in ('percentage_intellect', 'percentage_attack',
                                      'fixed_intellect', 'fixed_attack', 'jade_amount'):
                    data_now[k] = data_base[k] + ve
                else:
                    data_now[k] = ve
            else:
                data_now[k] = data_base[k]

        for v in UI_DATA.values():
            v.setStyleSheet("")
        ui_home.add.setStyleSheet('')
        exception = []
        for keys in UI_DATA:
            input_data(keys)

        if not (0 < data_now.get('in_lv', 1) < 41):
            exception.append(('in_lv', "1~40"))
        if not (0 < data_now.get('out_lv', 1) < 41):
            exception.append(('out_lv', '1~40'))
        if not (0 < data_now.get('ty_lv', 1) < 41):
            exception.append(('ty_lv', '1~40'))
        add = ui_home.add.text()
        try:
            data_now['add'] = int(add) if add else 0
        except ValueError:
            exception.append(('add', add))
        if exception:
            for key, tip in exception:
                if key in ('in_intellect', 'in_lv'):
                    ui_home.tabWidget.setCurrentIndex(0)
                elif key in ('out_medal', 'out_earp', 'out_passive', 'out_guild'):
                    ui_home.tabWidget.setCurrentIndex(1)
                elif key in ('nai_ba_guardian', 'nai_ba_ssp'):
                    naiba_setting()
                    ui_home.tabWidget.setCurrentIndex(2)
                UI_DATA[key].setText(tip)
                UI_DATA[key].setStyleSheet(
                    "background-color: #00aaff;"
                    "border:0px;"
                    "border-bottom: 3px solid red;")
        else:

            if type(data_now['percentage_attack']) is not list:
                data_now['percentage_attack'] = [data_now['percentage_attack']]
            if type(data_now['percentage_intellect']) is not list:
                data_now['percentage_intellect'] = [data_now['percentage_intellect']]
            if type(data_now['ty_percentage']) is not list:
                data_now['ty_percentage'] = [data_now['ty_percentage']]
            data_now['career'] = data_base['career']
            data_now['cp_arms'] = ui_home.cp_arm.isChecked()
            fn(data_now)

    return run_fn


def buff(data_now):
    cr = data_now['career']
    data_now['in_intellect'] += data_now["add"]
    data_now['out_intellect'] += data_now["add"]
    data_now['ty_intellect'] += data_now["add"]

    return {'zj': count_zj_buff(cr, data_now),
            'jt': count_jt_buff(cr, data_now),
            'ty': count_ty(data_now)
            }, \
        {
            'zj': count_zj_buff(cr, data_base),
            'jt': count_jt_buff(cr, data_base),
            'ty': count_ty(data_base)
        }


def value_to_str(data):
    if isinstance(data, dict):
        for key in data:
            data[key] = value_to_str(data[key])
    else:
        data = str(data)
    return data


def gap_set(gap):
    if isinstance(gap, dict):
        for key in gap:
            gap[key] = gap_set(gap[key])
    else:
        gap = "<font color='{}'>{:+d}<font>".format('#21f805' if gap >= 0 else '#f40c0c', gap)
    return gap


def current(data, gap):
    ui_home.buff_sg.setText(data['zj']['sg'])
    ui_home.buff_lz.setText(data['zj']['lz'])
    ui_home.buff_sg_cj.setText(gap['zj']['sg'])
    ui_home.buff_lz_cj.setText(gap['zj']['lz'])
    ui_home.yijue_lz.setText(data['ty'])
    ui_home.yijue_cj.setText(gap['ty'])
    ui_home.sanjue_lz_1.setText(data['san_one'])
    ui_home.sanjue_lz_1_cj.setText(gap['san_one'])
    ui_home.sanjue_lz_2.setText(data['san_two'])
    ui_home.sanjue_lz_2_cj.setText(gap['san_two'])
    ui_home.b1_sg.setText(data['jt']['sg'])
    ui_home.b1_lz.setText(data['jt']['lz'])
    ui_home.b1_sg_cj.setText(gap['jt']['sg'])
    ui_home.b1_lz_cj.setText(gap['jt']['lz'])
    ui_home.b2_sg.setText(data['z_jt']['sg'])
    ui_home.b2_lz.setText(data['z_jt']['lz'])
    ui_home.b2_sg_cj.setText(gap['z_jt']['sg'])
    ui_home.b2_lz_cj.setText(gap['z_jt']['lz'])


def set_naima(data, gap):
    current(data, gap)


def set_nailuo(data, gap):
    current(data, gap)
    ui_home.b3_sg.setText(data['p_jt']['sg'])
    ui_home.b3_lz.setText(data['p_jt']['lz'])
    ui_home.b3_lz_cj.setText(gap['p_jt']['lz'])
    ui_home.b3_sg_cj.setText(gap['p_jt']['sg'])


def set_naiba(data, gap):
    current(data, gap)


def set_naigong(data, gap):
    current(data, gap)


def clear():
    clear_text()
    clear_cj()
    ui_home.nailuo_button.setStyleSheet('')
    ui_home.naiba_button.setStyleSheet('')
    ui_home.naima_button.setStyleSheet('')
    ui_home.naigong_button.setStyleSheet('')


def naima_setting():
    clear()
    ui_home.tabWidget.removeTab(2)
    main_window.setWindowIcon(QIcon(":/png/84.PNG"))
    ui_home.label_6.setText('智力加减:')
    ui_home.label_3.setText('智力:')
    ui_home.label_17.setText('智力:')
    ui_home.label_15.setText('智力:')
    data_base['career'] = 'nai_ma'
    ui_home.naima_button.setStyleSheet('border:0px; border-radius: 0px;'
                                       ' padding-top:8px;'
                                       'padding-bottom:8px;'
                                       'border-left: 5px solid rgb(5, 229, 254);'
                                       'background-color:rgb(217, 217, 217);')
    ui_home.yijue.setTitle('圣光天启')
    ui_home.sanjue.setTitle('祈愿·天使赞歌')
    ui_home.yijue_icon.setPixmap(QtGui.QPixmap(":/png/23.PNG"))
    ui_home.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/350.PNG"))
    ui_home.b0.setTitle('勇气祝福')
    ui_home.label_35.setPixmap(QtGui.QPixmap(":/png/84.PNG"))
    ui_home.b1.setTitle('勇气祝福')
    ui_home.label_30.setPixmap(QtGui.QPixmap(":/png/84.PNG"))
    ui_home.b2.setTitle('勇气+颂歌')
    ui_home.b3.hide()


def nailuo_setting():
    clear()
    ui_home.tabWidget.removeTab(2)
    main_window.setWindowIcon(QIcon(":/png/719.PNG"))
    ui_home.label_6.setText('智力加减:')
    ui_home.label_3.setText('智力:')
    ui_home.label_17.setText('智力:')
    ui_home.label_15.setText('智力:')
    data_base['career'] = 'nai_luo'
    ui_home.yijue.setTitle('开幕！人偶剧场')
    ui_home.sanjue.setTitle('终幕！人偶剧场')
    ui_home.nailuo_button.setStyleSheet('border:0px; border-radius: 0px;'
                                        ' padding-top:8px;'
                                        'padding-bottom:8px;'
                                        'border-left: 5px solid rgb(5, 229, 254);'
                                        'background-color:rgb(217, 217, 217);')
    ui_home.yijue_icon.setPixmap(QtGui.QPixmap(":/png/757.PNG"))
    ui_home.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/838.PNG"))
    ui_home.b0.setTitle('禁忌诅咒')
    ui_home.b1.setTitle('禁忌诅咒')

    ui_home.label_35.setPixmap(QtGui.QPixmap(":/png/719.PNG"))
    ui_home.label_30.setPixmap(QtGui.QPixmap(":/png/719.PNG"))
    ui_home.b2.setTitle('禁忌诅咒+疯狂召唤')
    ui_home.b3.show()


def naiba_setting():
    clear()
    ui_home.tabWidget.insertTab(2, ui_home.tab3, '奶爸二觉')
    main_window.setWindowIcon(QIcon(":/png/111.PNG"))
    ui_home.label_6.setText('体精加减:')
    ui_home.label_3.setText('体精:')
    ui_home.label_17.setText('体精:')
    ui_home.label_15.setText('体精:')
    data_base['career'] = 'nai_ba'
    ui_home.naiba_button.setStyleSheet('border:0px; border-radius: 0px;'
                                       ' padding-top:8px;'
                                       'padding-bottom:8px;'
                                       'border-left: 5px solid rgb(5, 229, 254);'
                                       'background-color:rgb(217, 217, 217);')
    ui_home.yijue.setTitle('天启之珠')
    ui_home.sanjue.setTitle('生命礼赞:神威')
    ui_home.yijue_icon.setPixmap(QtGui.QPixmap(":/png/158.PNG"))
    ui_home.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/548.PNG"))
    ui_home.b0.setTitle('荣誉祝福')
    ui_home.label_35.setPixmap(QtGui.QPixmap(":/png/111.PNG"))
    ui_home.b1.setTitle('荣誉祝福')
    ui_home.label_30.setPixmap(QtGui.QPixmap(":/png/111.PNG"))
    ui_home.b2.setTitle('守护+荣誉祝福(24层)')
    ui_home.b3.hide()


def naigong_setting():
    clear()
    ui_home.tabWidget.removeTab(2)
    main_window.setWindowIcon(QIcon(":/png/14.PNG"))
    ui_home.label_6.setText('精神加减:')
    ui_home.label_3.setText('精神:')
    ui_home.label_17.setText('精神:')
    ui_home.label_15.setText('精神:')
    ui_home.naigong_button.setStyleSheet('border:0px; border-radius: 0px;'
                                         ' padding-top:8px;'
                                         'padding-bottom:8px;'
                                         'border-left: 5px solid rgb(5, 229, 254);'
                                         'background-color:rgb(217, 217, 217);')
    ui_home.yijue.setTitle('梦想的舞台')
    ui_home.sanjue.setTitle('终曲:霓虹蝶梦')
    ui_home.yijue_icon.setPixmap(QtGui.QPixmap(":/png/88.PNG"))
    ui_home.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/34.PNG"))
    ui_home.b0.setTitle('可爱节拍')
    ui_home.label_35.setPixmap(QtGui.QPixmap(":/png/14.PNG"))
    ui_home.b1.setTitle('可爱节拍')
    ui_home.label_30.setPixmap(QtGui.QPixmap(":/png/14.PNG"))
    ui_home.b2.setTitle('可爱节拍+燃情狂想曲')
    ui_home.b3.hide()
    data_base['career'] = 'nai_gong'


@input_validation
def button_count_clicked(data_now):
    now, base = buff(data_now)
    career = data_now['career']
    # 下面是 向下取整,还是四舍五入 有待研究
    if career == 'nai_ma':
        now['z_jt'] = {k: round(v * 1.15) for k, v in now['jt'].items()}
        base['z_jt'] = {k: round(v * 1.15) for k, v in base['jt'].items()}
        now['san_one'] = round(now['ty'] * 1.12)
        now['san_two'] = round(now['ty'] * 1.27)
        base['san_one'] = round(base['ty'] * 1.12)
        base['san_two'] = round(base['ty'] * 1.27)
        gap = diff_dict(base, now)
        set_naima(value_to_str(now), gap_set(gap))
    elif career == 'nai_luo':
        now['z_jt'] = {k: round(v * 1.25) for k, v in now['jt'].items()}
        now['p_jt'] = {k: round(v * 1.4375) for k, v in now['jt'].items()}
        now['san_one'] = round(now['ty'] * 1.11)
        now['san_two'] = round(now['ty'] * 1.26)
        base['z_jt'] = {k: round(v * 1.25) for k, v in base['jt'].items()}
        base['p_jt'] = {k: round(v * 1.4375) for k, v in base['jt'].items()}
        base['san_one'] = round(base['ty'] * 1.11)
        base['san_two'] = round(base['ty'] * 1.26)
        gap = diff_dict(base, now)
        set_nailuo(value_to_str(now), gap_set(gap))
    elif career == 'nai_ba':
        _ = data_base.copy()
        _['in_intellect'] = _['in_intellect'] + data_base['nai_ba_guardian'] + data_base['nai_ba_ssp'] * 24
        data_now['in_intellect'] = data_now['in_intellect'] + data_now['nai_ba_guardian'] + data_now['nai_ba_ssp'] * 24
        now['z_jt'] = count_jt_buff(career, data_now)
        base['z_jt'] = count_jt_buff(career, _)
        #######################################
        now['san_one'] = round(now['ty'] * 1.11)
        now['san_two'] = round(now['ty'] * 1.26)
        base['san_one'] = round(base['ty'] * 1.11)
        base['san_two'] = round(base['ty'] * 1.26)
        gap = diff_dict(base, now)
        set_naiba(value_to_str(now), gap_set(gap))
    elif career == 'nai_gong':
        now['z_jt'] = {k: round(v * 1.1) for k, v in now['jt'].items()}
        base['z_jt'] = {k: round(v * 1.1) for k, v in base['jt'].items()}
        now['san_one'] = round(now['ty'] * 1.11)
        now['san_two'] = round(now['ty'] * 1.26)
        base['san_one'] = round(base['ty'] * 1.11)
        base['san_two'] = round(base['ty'] * 1.26)
        gap = diff_dict(base, now)
        set_naigong(value_to_str(now), gap_set(gap))


def diff_dict(dict1, dict2):
    """计算两个嵌套字典的差值"""
    diff = {}
    for key in dict1:
        if isinstance(dict1[key], dict):
            diff[key] = diff_dict(dict1[key], dict2[key])
        else:
            diff[key] = dict2[key] - dict1[key]
    return diff


def count_buff(buff_amount, intellect, xs, xyz, cp_arms, arm=1.08):  # 这个arm参数仅用于临时修正奶爸的站街武器BUG
    x, y, z = xyz

    def count(fixed, bfb: list, basic_attack) -> int:
        old_buff = ((basic_attack + fixed) * ((intellect / xs) + 1))
        for n in bfb:
            old_buff *= (1 + n / 100)
        new_buff = basic_attack * ((intellect + x) / xs + 1) * (buff_amount + y) * z if buff_amount != 0 else 0
        bf = (old_buff + new_buff) * (arm if cp_arms else 1)

        return round(bf)

    return count


def count_zj_buff(cr: str, data) -> dict:
    arm = 1.008 if cr == 'nai_ba' else 1.08  # 奶爸武器bug
    count = count_buff(
        int(data['buff_amount'] * (1 + data['halo_amount'] / 100 + data['pet_amount'] / 100)),
        data['out_intellect'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['xyz'],
        data['cp_arms'],
        arm  # 奶爸武器bug
    )
    return {
        'sg': count(
            data['fixed_attack'],
            data['percentage_attack'],
            BASIC_DATA[cr]['san_gong'][data['out_lv'] - 1],

        ),

        'lz': count(
            data['fixed_intellect'],
            data['percentage_intellect'],
            BASIC_DATA[cr]['li_zhi'][data['out_lv'] - 1],
        )}


def count_jt_buff(cr, data) -> dict:
    count = count_buff(
        int(data['buff_amount'] * (
                1 + data['halo_amount'] / 100 + data['pet_amount'] / 100 + data['jade_amount'] / 100)),
        data['in_intellect'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['xyz'],
        data['cp_arms']
    )
    return {
        'sg': count(
            data['fixed_attack'],
            data['percentage_attack'],
            BASIC_DATA[cr]['san_gong'][data['in_lv'] - 1],
        ),
        'lz': count(
            data['fixed_intellect'],
            data['percentage_intellect'],
            BASIC_DATA[cr]['li_zhi'][data['in_lv'] - 1],
        )}


def count_ty(data) -> int:
    count = count_buff(
        int(data['buff_amount'] * (
                1 + data['halo_amount'] / 100 + data['pet_amount'] / 100 + data['jade_amount'] / 100)),
        data['ty_intellect'],
        BASIC_DATA['tai_yang']['xs'],
        BASIC_DATA['tai_yang']['xyz'],
        False)
    return count(data['ty_fixed'],
                 data['ty_percentage'],
                 BASIC_DATA['tai_yang']['li_zhi'][data['ty_lv'] - 1],
                 )


@input_validation
def is_contrast(data_now):
    global data_base
    data_base['cp_arms'] = ui_home.cp_arm.isChecked()
    for k, v in UI_DATA.items():
        v.setPlaceholderText(str(data_now[k]).replace('[', '').replace(']', ''))
        v.setText('')
    data_base = data_now.copy()
    clear_cj()


def clear_cj():
    ui_home.buff_sg_cj.setText('')
    ui_home.buff_lz_cj.setText('')
    ui_home.b1_lz_cj.setText('')
    ui_home.b1_sg_cj.setText('')
    ui_home.b2_lz_cj.setText('')
    ui_home.b2_sg_cj.setText('')
    ui_home.b3_sg_cj.setText('')
    ui_home.b3_lz_cj.setText('')
    ui_home.yijue_cj.setText('')
    ui_home.sanjue_lz_1_cj.setText('')
    ui_home.sanjue_lz_2_cj.setText('')


def clear_text():
    ui_home.buff_sg.setText('')
    ui_home.buff_lz.setText('')
    ui_home.b1_lz.setText('')
    ui_home.b1_sg.setText('')
    ui_home.b2_lz.setText('')
    ui_home.b2_sg.setText('')
    ui_home.b3_sg.setText('')
    ui_home.b3_lz.setText('')
    ui_home.yijue_lz.setText('')
    ui_home.sanjue_lz_1.setText('')
    ui_home.sanjue_lz_2.setText('')


def close_windows():
    QCoreApplication.instance().quit()


@input_validation
def save_data(data_now):
    if not path.exists(path.dirname(FILE_PATH)):
        makedirs(path.dirname(FILE_PATH))
    with open(FILE_PATH, "w+") as f:
        f.write(str(data_now))
    is_contrast()


def load_data():
    if not path.exists(path.dirname(FILE_PATH)):
        makedirs(path.dirname(FILE_PATH))
        with open(FILE_PATH, "w+") as file:
            file.write(str(data_base))
    with open(FILE_PATH, "r") as f:
        try:
            data_now = literal_eval(f.read())
        except:
            data_now = {}
    for k, v in data_now.items():
        if k in UI_DATA:
            UI_DATA[k].setText(str(v).replace('[', '').replace(']', ''))
    career = data_now.get('career', 'nai_ma')
    is_contrast()
    if career == 'nai_ma':
        naima_setting()
    elif career == 'nai_ba':
        naiba_setting()
    elif career == 'nai_luo':
        nailuo_setting()
    elif career == 'nai_gong':
        naigong_setting()


def lv_to():
    text = ui_home.zl_lv.text().replace(" ", "")

    if text.isdigit():
        ui_home.jt_lv.setText(str(int(text) + 14))


def intellect_to():
    if not ui_home.jt_zhili.text().startswith(('-', '+')):
        intellect = 0
        for le in ('out_medal', 'out_earp', 'out_passive', 'out_guild', 'out_intellect'):
            text = UI_DATA[le].text()
            intellect += int(text) if text.isdigit() else data_base.get(le, 0)
        text = UI_DATA['out_passive'].text()
        text = int(text) if text.isdigit() else data_base.get('out_passive', 0)
        ui_home.jt_zhili.setText(str(intellect))
        ui_home.ty_zhili.setText(str(intellect - text))


if __name__ == '__main__':
    app = QApplication(argv)
    main_window = RoundedWindow()
    ui_home.setupUi(main_window)
    main_window.setWindowTitle(' 奶量计算器')

    # 要检查的输入框
    UI_DATA = {
        'buff_amount': ui_home.buff_liang,
        'out_intellect': ui_home.zj_zhili,
        'out_lv': ui_home.zl_lv,

        'in_lv': ui_home.jt_lv,
        'ty_lv': ui_home.ty_lv,

        'halo_amount': ui_home.buff_gh,
        'pet_amount': ui_home.buff_cw,
        'jade_amount': ui_home.buff_bxy,

        'fixed_attack': ui_home.sg_guding,
        'fixed_intellect': ui_home.lz_guding,

        'percentage_attack': ui_home.sg_bfb,
        'percentage_intellect': ui_home.lz_bfb,

        'ty_fixed': ui_home.ty_lz,
        'ty_percentage': ui_home.ty_bfb,

        'out_medal': ui_home.zj_xz,
        'out_earp': ui_home.zj_eh,
        'out_passive': ui_home.zj_bd,
        'out_guild': ui_home.zj_gh,
        'nai_ba_guardian': ui_home.naiba_sh,
        'nai_ba_ssp': ui_home.naiba_ej,

        'ty_intellect': ui_home.ty_zhili,
        'in_intellect': ui_home.jt_zhili,  # 此项在最后

    }
    load_data()
    button_count_clicked()
    ####################
    ui_home.button_count.clicked.connect(button_count_clicked)
    ui_home.button_jc.clicked.connect(is_contrast)
    ui_home.button_close.clicked.connect(close_windows)
    ui_home.button_save.clicked.connect(save_data)
    ui_home.button_load.clicked.connect(load_data)
    ####################
    ui_home.nailuo_button.clicked.connect(nailuo_setting)
    ui_home.naima_button.clicked.connect(naima_setting)
    ui_home.naiba_button.clicked.connect(naiba_setting)
    ui_home.naigong_button.clicked.connect(naigong_setting)
    ####################
    ui_home.zl_lv.textChanged.connect(lv_to)
    ui_home.zj_xz.textChanged.connect(intellect_to)
    ui_home.zj_zhili.textChanged.connect(intellect_to)
    ui_home.zj_gh.textChanged.connect(intellect_to)
    ui_home.zj_eh.textChanged.connect(intellect_to)
    ui_home.zj_bd.textChanged.connect(intellect_to)

    ####################
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(10)  # 范围
    effect.setOffset(0, 0)  # 横纵,偏移量
    effect.setColor(Qt.black)  # 颜色
    ui_home.widget_1.setGraphicsEffect(effect)
    ######################
    main_window.show()
    app.exec_()
