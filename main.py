import sys
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect
from Widget import RoundedWindow
from UI import Ui_Form
from PyQt5.QtCore import Qt, QCoreApplication

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
contrast = {}


def input_validation(text):
    text = text.replace(" ", "")
    if text == "":
        return 0.0
    try:
        return float(text)
    except ValueError as e:
        raise e


def count_buff(lv, buff_amount, intellect, attack_fixed, ap_1, ap_2, ap_3, ap_4, ap_5):
    basic_attack = BASIC_DATA['nai_ma']['san_gong'][int(lv - 1) if 0 < int(lv - 1) < 41 else 0]
    old_buff = ((basic_attack + attack_fixed) * ((intellect / 665) + 1)) * ap_1 * ap_2 * ap_3 * ap_4 * ap_5
    new_buff = basic_attack * ((intellect + 4345) / 665 + 1) * (
            buff_amount + 3500) * 0.0000379 if buff_amount != 0 else 0
    buff = (old_buff + new_buff) * (1.08 if buff_amount != 0 else 1)
    return round(buff)


def count_zj_buff():
    return count_buff(
        input_validation(ui_home.zl_lv.text()),
        input_validation(ui_home.zl_buff.text()) * (1 + input_validation(ui_home.sg_buff_gh.text()) / 100 +
                                                    input_validation(ui_home.sg_buff_cw.text()) / 100),
        input_validation(ui_home.zj_zhili.text()),
        input_validation(ui_home.sg_guding.text()),
        1 + input_validation(ui_home.sg_bf_1.text()) / 100,
        1 + input_validation(ui_home.sg_bf_2.text()) / 100,
        1 + input_validation(ui_home.sg_bf_3.text()) / 100,
        1 + input_validation(ui_home.sg_bf_4.text()) / 100,
        1 + input_validation(ui_home.sg_bf_5.text()) / 100,

    )


def count_jt_buff():
    return count_buff(
        input_validation(ui_home.jt_lv.text()),
        input_validation(ui_home.zl_buff.text()) * (1 + input_validation(ui_home.sg_buff_gh.text()) / 100 +
                                                    input_validation(ui_home.sg_buff_bxy.text()) / 100 +
                                                    input_validation(ui_home.sg_buff_cw.text()) / 100
                                                    )

        ,
        input_validation(ui_home.jt_zhili.text()),
        input_validation(ui_home.sg_guding.text()),
        1 + input_validation(ui_home.sg_bf_1.text()) / 100,
        1 + input_validation(ui_home.sg_bf_2.text()) / 100,
        1 + input_validation(ui_home.sg_bf_3.text()) / 100,
        1 + input_validation(ui_home.sg_bf_4.text()) / 100,
        1 + input_validation(ui_home.sg_bf_5.text()) / 100,

    )


def button_count_clicked():
    try:
        global contrast
        zj_buff = count_zj_buff()
        jt_buff = count_jt_buff()
        ui_home.zj_show_sg.setText(str(zj_buff))
        ui_home.jt_show_sg.setText(str(jt_buff))
        ui_home.jt_show_zsg.setText(str(round(jt_buff * 1.15)))
        if contrast:
            zj_cj = zj_buff - contrast['zj']
            jt_cj = jt_buff - contrast['jt']
            jt_zcj = round((jt_buff - contrast['jt']) * 1.15)

            ui_home.zj_show_sg_cj.setText(f"<font color='#21f805' >+{zj_cj}<font>" if zj_cj > 0 else
                                          f"<font color='#f40c0c' >{zj_cj}<font>")
            ui_home.jt_show_sg_cj.setText(f"<font color='#21f805' >+{zj_cj}<font>" if jt_cj > 0 else
                                          f"<font color='#f40c0c' >{jt_cj}<font>")
            ui_home.jt_show_zsg_cj.setText(f"<font color='#21f805' >+{zj_cj}<font>" if jt_zcj > 0 else
                                           f"<font color='#f40c0c' >{jt_zcj}<font>")
    except Exception as e:
        print(e)


def is_contrast():
    global contrast
    contrast = {
        'jt': count_jt_buff(),
        'zj': count_zj_buff()
    }

    ui_home.zj_show_sg_cj.setText('')
    ui_home.jt_show_sg_cj.setText('')
    ui_home.jt_show_zsg_cj.setText('')


def close_windows():
    QCoreApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_home = Ui_Form()
    main_window = RoundedWindow()
    ui_home.setupUi(main_window)
    ####################
    ui_home.button_count.clicked.connect(button_count_clicked)
    ui_home.button_jc.clicked.connect(is_contrast)
    ui_home.button_close.clicked.connect(close_windows)
    ####################
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(10)  # 范围
    effect.setOffset(0, 0)  # 横纵,偏移量
    effect.setColor(Qt.black)  # 颜色
    ui_home.widget_1.setGraphicsEffect(effect)
    main_window.show()
    app.exec_()
