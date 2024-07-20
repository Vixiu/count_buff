from sys import argv

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication, QLineEdit, QListWidgetItem, QMessageBox

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5 import QtGui
from UI import Ui_widget


class RoundedWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        """鼠标弹起事件"""
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.move(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()

    def window_top(self, flag):
        if flag:
            self.windowHandle().setFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        else:
            self.windowHandle().setFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.repaint()


class BuffUI(Ui_widget):
    def __init__(self):
        self.input_data = None

    def init(self):
        #

        # 默认按钮绑定事件
        self.naima_button.clicked.connect(self.__naima_setting)
        self.naiba_button.clicked.connect(self.__naiba_setting)
        self.nailuo_button.clicked.connect(self.__nailuo_setting)
        self.naigong_button.clicked.connect(self.__naigong_setting)
        # 绑定
        self.zj_lv.textEdited.connect(self.__lv_to)
        self.zj_xz.textEdited.connect(self.__intellect_to)
        #  self.zj_zhili.textEdited.connect(self.__intellect_to)
        self.zj_gh.textEdited.connect(self.__intellect_to)
        self.zj_eh.textEdited.connect(self.__intellect_to)
        self.tabWidget.tabBarClicked.connect(self.__tab_widget)

        ########
        self.input_data = {
            "ty_intellect": self.ty_zhili,
            "in_intellect": self.jt_zhili,
            "buff_amount": self.buff_liang,
            "buff_wz": self.buff_wz,
            "out_intellect": self.zj_zhili,
            "out_lv": self.zj_lv,
            "add": self.add,
            "in_lv": self.jt_lv,
            "ty_lv": self.ty_lv,
            "ty3_lv": self.ty3_lv,
            "halo_amount": self.buff_gh,
            "pet_amount": self.buff_cw,
            "jade_amount": self.buff_bxy,
            "fixed_attack": self.sg_guding,
            "fixed_intellect": self.lz_guding,
            "percentage_attack": self.sg_bfb,
            "percentage_intellect": self.lz_bfb,
            "ty_fixed": self.ty_lz,
            "ty_percentage": self.ty_bfb,
            "out_medal": self.zj_xz,
            "out_earp": self.zj_eh,
            "out_guild": self.zj_gh,
            "nai_ba_guardian": self.naiba_sh,
            "nai_ba_ssp": self.naiba_ej,
            "cp_arms": self.cp_arm,
            "ty3_true": self.radioButton,
            "c_attack": self.c_sg,
            "c_intellect": self.c_lz,
            ###
            "lv_01": self.lv_01,
            "lv_02": self.lv_02,
            "lv_03": self.lv_03,
            "lv_04": self.lv_04,

        }
        self.__set_validator()

    def __tab_widget(self, index):
        if index == 2:
            self.__intellect_to()

    def add_config(self, name, select=False):
        item = QListWidgetItem(name)
        #  item.setFlags(item.flags() | Qt.ItemIsEditable)
        item.setTextAlignment(Qt.AlignCenter)
        self.config_list.addItem(item)
        QApplication.processEvents()
        self.config_list.update()
        self.config_list.repaint()
        item.setSelected(select)

    def get_value(self, name):
        if name not in self.input_data:
            raise ValueError(f"{name} is not in UI")
        if name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
            val = self.input_data[name].text()
            if val == '' or val in ("-", "+"):
                val = self.input_data[name].placeholderText()
            return [float(i) for i in val.split(",") if i] if val else []
        elif name in ("pet_amount", "halo_amount", "jade_amount"):
            val = self.input_data[name].text()
            if val == '' or val in ("-", "+"):
                val = self.input_data[name].placeholderText()
            return float(val) if val else 0.0
        elif name == "cp_arms":
            return self.input_data[name].isChecked()
        elif name == "ty3_true":
            return self.input_data[name].isChecked()
        elif name == "buff_amount":
            val = self.input_data[name].text()
            if val == '' or val in ("-", "+"):
                val = self.input_data[name].placeholderText()
            elif val.startswith('+') or val.startswith('-'):
                return int(float(val)) + int(self.input_data[name].placeholderText())
            return int(float(val)) if val else 0
        else:
            val = self.input_data[name].text()
            if val == '' or val in ("-", "+"):
                val = self.input_data[name].placeholderText()
            return int(float(val)) if val else 0

    def get_values(self) -> dict:
        return {name: self.get_value(name) for name in self.input_data}

    def set_value(self, name, value):
        if name not in self.input_data:
            print(f"{name} is not in UI")
        elif name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
            self.input_data[name].setText(",".join([str(i) for i in value]))
        elif name == "cp_arms":
            self.input_data[name].setChecked(value)
        elif name == 'ty3_true':
            if value:
                self.radioButton.setChecked(True)
            else:
                self.radioButton_2.setChecked(True)
        elif name in ("c_attack", "c_intellect"):
            self.input_data[name].setPlaceholderText(str(value))
            self.input_data[name].setText('')
        elif name == "add_buff_amount" or name == 'add':
            pass
        else:
            self.input_data[name].setText(str(value))

    def set_values(self, values: dict):
        for name, value in values.items():
            self.set_value(name, value)

    def set_placeholder_text(self, name, text):
        if name not in self.input_data:
            raise ValueError(f"{name} is not in UI")
        if name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
            self.input_data[name].setPlaceholderText(",".join([str(i) for i in text]))
            self.input_data[name].setText('')
        elif name in ("cp_arms", "ty3_true", "add", "add_buff_amount"):
            return
        else:
            self.input_data[name].setPlaceholderText(str(text))
            self.input_data[name].setText('')

    def set_placeholder_texts(self, values: dict):
        for name, value in values.items():
            self.set_placeholder_text(name, value)

    def set_show_text(self, data, gap):
        self.buff_sg.setText(data['zj']['sg'])
        self.buff_lz.setText(data['zj']['lz'])
        self.buff_sg_cj.setText(gap['zj']['sg'])
        self.buff_lz_cj.setText(gap['zj']['lz'])
        self.yijue_lz.setText(data['ty'])
        self.yijue_cj.setText(gap['ty'])
        self.sanjue_lz_1.setText(data['ty3'])
        self.sanjue_lz_1_cj.setText(gap['ty3'])
        self.b1_sg.setText(data['jt']['sg'])
        self.b1_lz.setText(data['jt']['lz'])
        self.b1_sg_cj.setText(gap['jt']['sg'])
        self.b1_lz_cj.setText(gap['jt']['lz'])
        self.b2_sg.setText(data['z_jt']['sg'])
        self.b2_lz.setText(data['z_jt']['lz'])
        self.b2_sg_cj.setText(gap['z_jt']['sg'])
        self.b2_lz_cj.setText(gap['z_jt']['lz'])
        self.label_28.setText(data['resident'])
        self.label_43.setText(data['burst'])
        self.label_41.setText(gap['resident'])
        self.label_44.setText(gap['burst'])
        if 'p_jt' in data:
            self.b3_sg.setText(data['p_jt']['sg'])
            self.b3_lz.setText(data['p_jt']['lz'])
            self.b3_lz_cj.setText(gap['p_jt']['lz'])
            self.b3_sg_cj.setText(gap['p_jt']['sg'])

    def clear_left_button_style(self):
        """
        清除选择职业
        :return:
        """
        self.nailuo_button.setStyleSheet('')
        self.naiba_button.setStyleSheet('')
        self.naima_button.setStyleSheet('')
        self.naigong_button.setStyleSheet('')

    def clear_input_text(self):
        pass

    def clear_show_text(self):
        """
        清除输入文本
        :return:
        """
        self.buff_sg.setText('')
        self.buff_lz.setText('')
        self.b1_lz.setText('')
        self.b1_sg.setText('')
        self.b2_lz.setText('')
        self.b2_sg.setText('')
        self.b3_sg.setText('')
        self.b3_lz.setText('')
        self.yijue_lz.setText('')
        self.sanjue_lz_1.setText('')
        self.add.setText('')
        self.add_1.setText('1')
        self.add_2.setText('100')
        self.add_3.setText('1')
        self.lv_01.setText('')
        self.lv_02.setText('')
        self.lv_03.setText('')
        self.lv_04.setText('')

    def clear_show_hold_text(self):
        """
        清除差距文本
        :return:
        """
        self.buff_sg_cj.setText('')
        self.buff_lz_cj.setText('')
        self.b1_lz_cj.setText('')
        self.b1_sg_cj.setText('')
        self.b2_lz_cj.setText('')
        self.b2_sg_cj.setText('')
        self.b3_sg_cj.setText('')
        self.b3_lz_cj.setText('')
        self.yijue_cj.setText('')
        self.sanjue_lz_1_cj.setText('')
        self.label_41.setText('')
        self.label_44.setText('')

    def clear_all_text(self):
        """
        清除全部
        :return:
        """
        self.clear_show_hold_text()
        self.clear_show_text()
        self.clear_input_text()

    def __intellect_to(self):
        intellect = 0
        for le in ('out_medal', 'out_earp', 'out_guild', 'out_intellect'):
            text = self.get_value(le)
            intellect += int(text)
        lv = self.get_value('lv_02')
        intellect += (14 + lv // 2 * 23 + ((lv - 1) // 2) * 22)
        self.jt_zhili.setText(str(intellect))
        self.ty_zhili.setText(str(intellect))

    def __lv_to(self):
        lv_text = self.zj_lv.text()
        if lv_text:
            value = int(lv_text) + 14
            if value <= 40:
                self.jt_lv.setText(str(value))

    def __naima_setting(self):
        self.tabWidget.setTabVisible(1, True)
        #
        self.lb_01.setText('Lv15:启示:颂歌')
        self.lb_02.setText('Lv50:虔诚信念')
        self.lb_03.setText('Lv75:大天使庇护')
        self.lb_04.setText('Lv95:圣天使之光')
        self.zj_bd.setText('虔诚信念')
        #
        self.tabWidget.setTabVisible(3, False)
        self.tabWidget.setCurrentIndex(0)
        self.clear_all_text()
        self.clear_left_button_style()

        self.label_6.setText('智力加减:')
        self.label_3.setText('智力:')
        self.label_17.setText('智力:')
        self.label_15.setText('智力:')
        self.naima_button.setStyleSheet('border:0px; border-radius: 0px;'
                                        ' padding-top:8px;'
                                        'padding-bottom:8px;'
                                        'border-left: 5px solid #55ff7f;'
                                        'background-color:rgb(217, 217, 217);')
        self.yijue.setText('圣光天启')
        self.sanjue.setText('祈愿·天使赞歌')
        self.yijue_icon.setPixmap(QtGui.QPixmap(":/png/23.PNG"))
        self.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/350.PNG"))
        self.buff_name.setText('勇气祝福')
        self.buff_icon.setPixmap(QtGui.QPixmap(":/png/84.PNG"))
        self.buff_gain.setText('勇气+颂歌')

    def __nailuo_setting(self):
        self.tabWidget.setTabVisible(1, True)
        #
        self.lb_01.setText('Lv15:人偶操纵者')
        self.lb_02.setText('Lv50:少女的爱')
        self.lb_03.setText('Lv75:冥月绽放')
        self.lb_04.setText('Lv95:不祥的微笑')
        self.zj_bd.setText('少女的爱')
        #
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabVisible(3, False)

        self.clear_all_text()
        self.clear_left_button_style()

        #self.setWindowIcon(QIcon(":/png/719.PNG"))
        self.label_6.setText('智力加减:')
        self.label_3.setText('智力:')
        self.label_17.setText('智力:')
        self.label_15.setText('智力:')
        self.yijue.setText('开幕！人偶剧场')
        self.sanjue.setText('终幕！人偶剧场')
        self.nailuo_button.setStyleSheet('border:0px; border-radius: 0px;'
                                         ' padding-top:8px;'
                                         'padding-bottom:8px;'
                                         'border-left: 5px solid #55ff7f;'
                                         'background-color:rgb(217, 217, 217);')
        self.yijue_icon.setPixmap(QtGui.QPixmap(":/png/757.PNG"))
        self.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/838.PNG"))
        self.buff_name.setText('禁忌诅咒')
        self.buff_icon.setPixmap(QtGui.QPixmap(":/png/719.PNG"))
        self.buff_gain.setText('禁忌诅咒+疯狂召唤')

    def __naiba_setting(self):
        self.tabWidget.setTabVisible(1, False)
        #
        self.lb_01.setText('Lv15:守护恩赐')
        self.lb_02.setText('Lv50:信念光环')
        self.lb_03.setText('信仰之翼')
        self.lb_04.setText('Lv95:神之代行者')
        self.zj_bd.setText('待开发')
        # self.zj_bd.setText('Lv50:信念光环')
        #
        self.tabWidget.setTabVisible(3, True)
        self.tabWidget.setCurrentIndex(0)
        self.clear_all_text()
        self.clear_left_button_style()
        # self.setWindowIcon(QIcon(":/png/111.PNG"))
        self.label_6.setText('体精加减:')
        self.label_3.setText('体精:')
        self.label_17.setText('体精:')
        self.label_15.setText('体精:')
        self.naiba_button.setStyleSheet('border:0px; border-radius: 0px;'
                                        'padding-top:8px;'
                                        'padding-bottom:8px;'
                                        'border-left: 5px solid #55ff7f;'
                                        'background-color:rgb(217, 217, 217);')
        self.yijue.setText('天启之珠')
        self.sanjue.setText('生命礼赞:神威')
        self.yijue_icon.setPixmap(QtGui.QPixmap(":/png/158.PNG"))
        self.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/548.PNG"))
        self.buff_name.setText('荣誉祝福')
        self.buff_icon.setPixmap(QtGui.QPixmap(":/png/111.PNG"))

        self.buff_gain.setText('守护+荣誉祝福(24层)')

    def __naigong_setting(self):
        self.tabWidget.setTabVisible(1, True)
        #
        self.lb_01.setText('Lv15:多彩感性')
        self.lb_02.setText('Lv50:明星气场')
        self.lb_03.setText('Lv75:崭新曲风')
        self.lb_04.setText('Lv95:和茉霓之歌')
        self.zj_bd.setText('明星气场')
        #
        self.tabWidget.setCurrentIndex(0)
        self.clear_all_text()
        self.clear_left_button_style()
        self.tabWidget.setTabVisible(3, False)
        # self.setWindowIcon(QIcon(":/png/14.PNG"))
        self.label_6.setText('精神加减:')
        self.label_3.setText('精神:')
        self.label_17.setText('精神:')
        self.label_15.setText('精神:')
        self.naigong_button.setStyleSheet('border:0px; border-radius: 0px;'
                                          ' padding-top:8px;'
                                          'padding-bottom:8px;'
                                          'border-left: 5px solid #55ff7f;'
                                          'background-color:rgb(217, 217, 217);')
        self.yijue.setText('梦想的舞台')
        self.sanjue.setText('终曲:霓虹蝶梦')
        self.yijue_icon.setPixmap(QtGui.QPixmap(":/png/88.PNG"))
        self.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/34.PNG"))
        self.buff_name.setText('可爱节拍')
        self.buff_icon.setPixmap(QtGui.QPixmap(":/png/14.PNG"))

        self.buff_gain.setText('可爱节拍+燃情狂想曲')

    def __set_validator(self):
        def float_validator(input_box: QLineEdit):
            text = input_box.text().replace('。', '.').replace(' ', '')
            try:
                float(text)
                input_box.setText(text)
            except ValueError:
                input_box.setText(text[:-1])

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

        # 整数类型
        self.buff_liang.setValidator(QtGui.QIntValidator())
        self.add.setValidator(QtGui.QIntValidator())
        self.zj_zhili.setValidator(QtGui.QIntValidator())
        self.zj_xz.setValidator(QtGui.QIntValidator())
        self.zj_eh.setValidator(QtGui.QIntValidator())
        self.zj_gh.setValidator(QtGui.QIntValidator())
        self.naiba_ej.setValidator(QtGui.QIntValidator())
        self.naiba_sh.setValidator(QtGui.QIntValidator())
        self.jt_zhili.setValidator(QtGui.QIntValidator())
        self.ty_zhili.setValidator(QtGui.QIntValidator())
        self.ty3_lv.setValidator(QtGui.QIntValidator())
        self.sg_guding.setValidator(QtGui.QIntValidator())
        self.lz_guding.setValidator(QtGui.QIntValidator())
        self.ty_lz.setValidator(QtGui.QIntValidator())
        self.c_sg.setValidator(QtGui.QIntValidator())
        self.c_lz.setValidator(QtGui.QIntValidator())
        self.lv_01.setValidator(QtGui.QIntValidator())
        self.lv_02.setValidator(QtGui.QIntValidator())
        self.lv_03.setValidator(QtGui.QIntValidator())
        self.lv_04.setValidator(QtGui.QIntValidator())
        self.add_1.setValidator(QtGui.QIntValidator())
        self.add_2.setValidator(QtGui.QIntValidator())
        self.add_3.setValidator(QtGui.QIntValidator())

        # 浮点数
        self.buff_gh.textEdited.connect(lambda: float_validator(self.buff_gh))
        self.buff_cw.textEdited.connect(lambda: float_validator(self.buff_cw))
        self.buff_bxy.textEdited.connect(lambda: float_validator(self.buff_bxy))
        self.buff_wz.textEdited.connect(lambda: float_validator(self.buff_wz))
        # 等级
        self.jt_lv.textEdited.connect(lambda: lv_validator(self.jt_lv))
        self.ty_lv.textEdited.connect(lambda: lv_validator(self.ty_lv))
        self.zj_lv.textEdited.connect(lambda: lv_validator(self.zj_lv))

        # 百分比
        self.lz_bfb.textEdited.connect(lambda: percent_sign_validator(self.lz_bfb))
        self.sg_bfb.textEdited.connect(lambda: percent_sign_validator(self.sg_bfb))
        self.ty_bfb.textEdited.connect(lambda: percent_sign_validator(self.ty_bfb))
        # buff量与智力增加
