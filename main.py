from os import getenv, path, makedirs
from sys import argv
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect
from Widget import RoundedWindow
from UI import Ui_Form
from PyQt5.QtCore import Qt, QCoreApplication

FILE_PATH = rf'{getenv("APPDATA")}\count_buff\data.json'
ui_home = Ui_Form()

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
        'intellect_xyz': (4345.544, 3500, 0.0000379)
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
UI_DATA = {}
####
data_now = {
    'buff_amount': 0,
    'out_intellect': 0,
    'out_lv': 1,
    'out_medal': 50,
    'out_earp': 172,
    'out_passive': 554,
    'out_guild': 80,

    'in_intellect': 0,
    'in_lv': 1,
    #  'in_ty_lv': 1,
    'halo_amount': 0,
    'pet_amount': 0,
    'jade_amount': 0,
    'fixed_attack': 0,
    'fixed_intellect': 0,
    'percentage_attack': [],
    'percentage_intellect': [],
    'cp_arms': True
}
# 设为基础后的数据
data_base = {}

career = 'nai_ma'


def put_exception(fn):
    def ex():
        try:
            fn()
        except Exception as e:
            print(e)
        #    traceback.print_exc()

    return ex


def input_validation(fn):
    # 因为还要对输入数据在进行一次判断，所以不在输入层面就进行效验
    def validation(text: str):
        if ',' in text:
            return False, [eval(i) for i in text.split(',')]
        elif text.startswith('+') or text.startswith('-'):
            return True, eval(text)
        elif text.isdigit() or ('.' in text and text.count('.') == 1):
            return False, eval(text)
        else:
            return False, "非法字符"

    def run_fn():
        global data_now

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

        for v in UI_DATA.values():
            v.setStyleSheet("")
        exception = []
        for keys in UI_DATA:
            input_data(keys)

        if type(data_now['percentage_attack']) is not list:
            data_now['percentage_attack'] = [data_now['percentage_attack']]
        if type(data_now['percentage_intellect']) is not list:
            data_now['percentage_intellect'] = [data_now['percentage_intellect']]

        if not (0 < data_now['in_lv'] < 41):
            exception.append(('in_lv', '1~40'))
        if not (0 < data_now['out_lv'] < 41):
            exception.append(('out_lv', '1~40'))

        if exception:
            for key, tip in exception:
                UI_DATA[key].setText(tip)
                UI_DATA[key].setStyleSheet("font-size: 12px;"
                                           "background-color: #00aaff;"
                                           "border:0px;"
                                           "border-bottom: 3px solid red;")

        else:
            fn()

    return run_fn


@input_validation
def button_count_clicked():
    buff = {
        'zj': count_zj_buff(career, data_now),
        'jt': count_jt_buff(career, data_now),
    }
    buff['z_jt'] = (str(round(int(buff['jt'][0]) * 1.15)), str(round(int(buff['jt'][1]) * 1.15)))

    ui_home.sg_zj.setText(buff['zj'][0])
    ui_home.lz_zj.setText(buff['zj'][1])
    ui_home.sg_jt.setText(buff['jt'][0])
    ui_home.lz_jt.setText(buff['jt'][1])
    ui_home.zsg.setText(buff['z_jt'][0])
    ui_home.zlz.setText(buff['z_jt'][1])

    if data_base:
        base = {
            'zj': count_zj_buff(career, data_base),
            'jt': count_jt_buff(career, data_base),
        }
        base['z_jt'] = (str(round(int(base['jt'][0]) * 1.15)), str(round(int(base['jt'][1]) * 1.15)))
        gap = {k: (int(v[0]) - int(base[k][0]), int(v[1]) - int(base[k][1])) for k, v in buff.items()}
        ui_home.sg_zj_cj.setText("<font color='{}' >{:+d}<font>".format(
            '#21f805' if gap['zj'][0] > 0 else '#f40c0c', gap['zj'][0]))
        ui_home.lz_zj_cj.setText("<font color='{}' >{:+d}<font>".format(
            '#21f805' if gap['zj'][1] > 0 else '#f40c0c', gap['zj'][1]))
        ui_home.sg_jt_cj.setText("<font color='{}' >{:+d}<font>".format(
            '#21f805' if gap['jt'][0] > 0 else '#f40c0c', gap['jt'][0]))
        ui_home.lz_jt_cj.setText("<font color='{}' >{:+d}<font>".format(
            '#21f805' if gap['jt'][1] > 0 else '#f40c0c', gap['jt'][1]))
        ui_home.zsg_cj.setText("<font color='{}' >{:+d}<font>".format(
            '#21f805' if gap['z_jt'][0] > 0 else '#f40c0c', gap['z_jt'][0]))
        ui_home.zlz_cj.setText("<font color='{}' >{:+d}<font>".format(
            '#21f805' if gap['z_jt'][1] > 0 else '#f40c0c', gap['z_jt'][1]))


def count_buff(lv, buff_amount, intellect, cp_arms=True):
    def count(fixed, bfb, basic_list, xs, xyz) -> str:
        x, y, z = xyz
        basic_attack = basic_list[lv - 1]
        old_buff = ((basic_attack + fixed) * ((intellect / xs) + 1))
        for n in bfb:
            old_buff *= (1 + n / 100)
        new_buff = basic_attack * ((intellect + x) / xs + 1) * (buff_amount + y) * z if buff_amount != 0 else 0
        bf = (old_buff + new_buff) * (1.08 if cp_arms else 1)
        return str(round(bf))

    return count


def count_zj_buff(cr, data):
    count = count_buff(
        data['out_lv'],
        int(data['buff_amount'] * (1 + data['halo_amount'] / 100 + data['pet_amount'] / 100)),
        data['out_intellect'],
    )

    return count(
        data['fixed_attack'],
        data['percentage_attack'],
        BASIC_DATA[cr]['san_gong'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['attack_xyz'],
    ), count(
        data['fixed_intellect'],
        data['percentage_intellect'],
        BASIC_DATA[cr]['li_zhi'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['intellect_xyz'],
    )


def count_jt_buff(cr, data):
    count = count_buff(
        data['in_lv'],
        int(data['buff_amount'] * (
                1 + data['halo_amount'] / 100 + data['pet_amount'] / 100 + data['jade_amount'] / 100)),
        data['in_intellect'],
    )

    return count(
        data['fixed_attack'],
        data['percentage_attack'],
        BASIC_DATA[cr]['san_gong'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['attack_xyz'],
    ), count(
        data['fixed_intellect'],
        data['percentage_intellect'],
        BASIC_DATA[cr]['li_zhi'],
        BASIC_DATA[cr]['xs'],
        BASIC_DATA[cr]['intellect_xyz'],
    )


@input_validation
def is_contrast():
    global data_base, data_now
    for k, v in data_now.items():
        UI_DATA[k].setPlaceholderText(str(v).replace('[', '').replace(']', ''))
        UI_DATA[k].setText('')
    data_base = data_now.copy()
    ui_home.sg_zj_cj.setText("")
    ui_home.lz_zj_cj.setText("")
    ui_home.sg_jt_cj.setText("")
    ui_home.lz_jt_cj.setText("")
    ui_home.zsg_cj.setText("")
    ui_home.zlz_cj.setText("")


def close_windows():
    QCoreApplication.instance().quit()


@input_validation
def save_data():
    if not path.exists(path.dirname(FILE_PATH)):
        makedirs(path.dirname(FILE_PATH))
    with open(FILE_PATH, "w+") as f:
        f.write(str(data_now))


def load_data():
    global data_now
    with open(FILE_PATH, "r") as f:
        data_now = eval(f.read())
    for k, v in data_now.items():
        UI_DATA[k].setText(str(v).replace('[', '').replace(']', ''))
    button_count_clicked()
    is_contrast()


def lv_to():
    text = ui_home.zl_lv.text().replace(" ", "")
    if text.isdigit():
        ui_home.jt_lv.setText(str(int(text) + 14))


def intellect_to():
    if not ui_home.jt_zhili.text().startswith(('-', '+')):
        intellect = 0
        for le in ('out_medal', 'out_earp', 'out_passive', 'out_guild', 'out_intellect'):
            if UI_DATA[le].text().isdigit():
                intellect += int(UI_DATA[le].text()) if UI_DATA[le].text().isdigit() else 0
            else:
                intellect += data_base.get(le, 0)
        ui_home.jt_zhili.setText(str(intellect))


def calculate_intellect():
    intellect = 0
    zhili_text = ui_home.jt_zhili.text()
    if not zhili_text.startswith(('-', '+')):
        for le in ('out_medal', 'out_earp', 'out_passive', 'out_guild', 'out_intellect'):
            le_text = UI_DATA[le].text()
            if le_text.isdigit():
                intellect += int(le_text)
        ui_home.jt_zhili.setText(str(intellect))


if __name__ == '__main__':
    app = QApplication(argv)
    main_window = RoundedWindow()
    ui_home.setupUi(main_window)
    UI_DATA = {
        'buff_amount': ui_home.buff_liang,
        'out_intellect': ui_home.zj_zhili,
        'out_lv': ui_home.zl_lv,
        'in_intellect': ui_home.jt_zhili,
        'in_lv': ui_home.jt_lv,
        #   'in_ty_lv': ui_home.jt_ty_lv,

        'halo_amount': ui_home.buff_gh,
        'pet_amount': ui_home.buff_cw,
        'jade_amount': ui_home.buff_bxy,

        'fixed_attack': ui_home.sg_guding,
        'fixed_intellect': ui_home.lz_guding,

        'percentage_attack': ui_home.sg_bfb,
        'percentage_intellect': ui_home.lz_bfb,

        'out_medal': ui_home.zj_xz,
        'out_earp': ui_home.zj_eh,
        'out_passive': ui_home.zj_bd,
        'out_guild': ui_home.zj_gh,
    }
    if not path.exists(path.dirname(FILE_PATH)):
        makedirs(path.dirname(FILE_PATH))
        with open(FILE_PATH, "w+") as f:
            f.write(str(data_now))
    load_data()
    ####################
    ui_home.button_count.clicked.connect(button_count_clicked)
    ui_home.button_jc.clicked.connect(is_contrast)
    ui_home.button_close.clicked.connect(close_windows)
    ui_home.button_save.clicked.connect(save_data)
    ui_home.button_load.clicked.connect(load_data)
    ui_home.zl_lv.textChanged.connect(lv_to)
    # -
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

    main_window.show()
    app.exec_()
